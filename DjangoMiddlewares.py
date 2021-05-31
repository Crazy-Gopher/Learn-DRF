## Middlewares
A Middleware is a regular Python class that hooks into Django’s request/response life cycle. Those classes holds pieces of code that are processed upon every request/response your Django application handles.

The Middleware classes doesn’t have to subclass anything and it can live anywhere in your Python path. The only thing Django cares about is the path you register in the project settings MIDDLEWARE_CLASSES.

Each middleware component is responsible for doing some specific function. For example, Django includes a middleware component, AuthenticationMiddleware, that associates users with requests using sessions.

Called during request:
                process_request(request)
                process_view(request, view_func, view_args, view_kwargs)
Called during response:
                process_exception(request, exception) (only if the view raised an exception)
                process_template_response(request, response) (only for template responses)
                process_response(request, response)


## How it works?

The Middlware classes are called twice during the request/response life cycle. For that reason, the order you define the Middlwares in the MIDDLEWARE_CLASSES configuration is important.

Let’s have a look on the built-in Middleware classes the django-admin startproject command sets up:

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

During the request cycle, the Middleware classes are executed top-down, meaning it will first execute SecurityMiddleware, then SessionMiddleware all the way until XFrameOptionsMiddleware. For each of the Middlewares it will execute the process_request() and process_view() methods.

At this point, Django will do all the work on your view function. After the work is done (e.g. querying the database, paginating results, processing information, etc), it will return a response for the client.

During the response cycle, the Middleware classes are executed bottom-up, meaning it will first execute XFrameOptionsMiddleware, then MessageMiddleware all the way until SecurityMiddleware. For each of the Middlewares it will execute the process_exception(), process_template_response() and process_response() methods.

Finally Django will deliver the response for the client. It is important to note that process_exception() is only executed if a exception occurs inside the view function and process_template_response() is only executed if there is a template in the response.


## New way of writing middleware:
1. A middleware can be written as a function that looks like this:

def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
	

2. Or it can be written as a class whose instances are callable, like this:

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

Note: The get_response callable provided by Django might be the actual view (if this is the last listed middleware) or it might be the next middleware in the chain. The current middleware doesn’t need to know or care what exactly it is, just that it represents whatever comes next.













wherever/you/want/to/put/Middleware.py
import requests
from django.conf import settings

class StackOverflowMiddleware(object):
    def process_exception(self, request, exception):
        if settings.DEBUG:
            intitle = u'{}: {}'.format(exception.__class__.__name__,  exception.message)
            print intitle

            url = 'https://api.stackexchange.com/2.2/search'
            headers = { 'User-Agent': 'github.com/vitorfs/seot' }
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'pagesize': 3,
                'tagged': 'python;django',
                'intitle': intitle
            }

            r = requests.get(url, params=params, headers=headers)
            questions = r.json()

            print ''

            for question in questions['items']:
                print question['title']
                print question['link']
                print ''

        return None


1. process_request(request)
                request is an HttpRequest object.

                process_request() is called on each request, before Django decides which view to execute.

                It should return either None or an HttpResponse object. If it returns None, Django will continue processing this request, executing any other process_request() middleware, then, process_view() middleware, and finally, the appropriate view. If it returns an HttpResponse object, Django won’t bother calling any other request, view or exception middleware, or the appropriate view; it’ll apply response middleware to that HttpResponse, and return the result.


2. process_view(request, view_func, view_args, view_kwargs)
                request is an HttpRequest object. view_func is the Python function that Django is about to use. (It’s the actual function object, not the name of the function as a string.) view_args is a list of positional arguments that will be passed to the view, and view_kwargs is a dictionary of keyword arguments that will be passed to the view. Neither view_args nor view_kwargs include the first view argument (request).

                process_view() is called just before Django calls the view.

                It should return either None or an HttpResponse object. If it returns None, Django will continue processing this request, executing any other process_view() middleware and, then, the appropriate view. If it returns an HttpResponse object, Django won’t bother calling any other view or exception middleware, or the appropriate view; it’ll apply response middleware to that HttpResponse, and return the result.


Note: Accessing request.POST or request.REQUEST inside middleware from process_request or process_view will prevent any view running after the middleware from being able to modify the upload handlers for the request, and should normally be avoided.


3. process_template_response(request, response):
                request is an HttpRequest object. response is the TemplateResponse(django.template.response.TemplateResponse) object (or equivalent) returned by a Django view or by a middleware.
                process_template_response() is called just after the view has finished executing, if the response instance has a render() method, indicating that it is a TemplateResponse or equivalent.


4. process_response(request, response):
                request is an HttpRequest object. response is the HttpResponse or StreamingHttpResponse object returned by a Django view or by a middleware.
                process_response() is called on all responses before they’re returned to the browser.

                It must return an HttpResponse or StreamingHttpResponse object. It could alter the given response, or it could create and return a brand-new HttpResponse or StreamingHttpResponse.

                Unlike the process_request() and process_view() methods, the process_response() method is always called, even if the process_request() and process_view() methods of the same middleware class were skipped (because an earlier middleware method returned an HttpResponse). In particular, this means that your process_response() method cannot rely on setup done in process_request().

                Finally, remember that during the response phase, middleware are applied in reverse order, from the bottom up. This means classes defined at the end of MIDDLEWARE_CLASSES will be run first.

5. process_exception(request, exception)

                request is an HttpRequest object. exception is an Exception object raised by the view function.

                Django calls process_exception() when a view raises an exception. process_exception() should return either None or an HttpResponse object. If it returns an HttpResponse object, the template response and response middleware will be applied, and the resulting response returned to the browser. Otherwise, default exception handling kicks in.


    def process_response(self, request, response):
        """
        When the status code of the response is 404, it may redirect to a path
        with an appended slash if should_redirect_with_slash() returns True.
        """
        # If the given URL is "Not Found", then check if we should redirect to
        # a path with a slash appended.
        if response.status_code == 404:
            if self.should_redirect_with_slash(request):
                return self.response_redirect_class(self.get_full_path_with_slash(request))

        # Add the Content-Length header to non-streaming responses if not
        # already set.
        if not response.streaming and not response.has_header('Content-Length'):
            response['Content-Length'] = str(len(response.content))

        return response

    def process_response(self, request, response):
        """Send broken link emails for relevant 404 NOT FOUND responses."""
        if response.status_code == 404 and not settings.DEBUG:
            domain = request.get_host()
           path = request.get_full_path()
            referer = request.META.get('HTTP_REFERER', '')

            if not self.is_ignorable_request(request, path, domain, referer):
                ua = request.META.get('HTTP_USER_AGENT', '<none>')
                ip = request.META.get('REMOTE_ADDR', '<none>')
                mail_managers(
                    "Broken %slink on %s" % (
                        ('INTERNAL ' if self.is_internal_request(domain, referer) else ''),
                        domain
                    ),
                    "Referrer: %s\nRequested URL: %s\nUser agent: %s\n"
                    "IP address: %s\n" % (referer, path, ua, ip),
                    fail_silently=True,
                )
        return response

    def process_response(self, request, response):
        if not getattr(request, 'csrf_cookie_needs_reset', False):
            if getattr(response, 'csrf_cookie_set', False):
                return response

        if not request.META.get("CSRF_COOKIE_USED", False):
            return response

        # Set the CSRF cookie even if it's already set, so we renew
        # the expiry timer.
        self._set_token(request, response)
        response.csrf_cookie_set = True
        return response


Use-cases:
1. We can create a middleware to log the time for processing a request(set time in process request and then check in process response)
Monitoring request latency
2. We can send a jwt refresh token to each request using middleware process response
