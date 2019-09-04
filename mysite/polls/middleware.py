import time
from django.utils.deprecation import MiddlewareMixin
class CustomMiddleware(object):
    def __init__(self, get_response):
        print("Custom middle-ware __init__")
        self.get_response = get_response
 
    def __call__(self, request):
        response = self.get_response(request)
        print("Custom middle-ware __call__")
        return response

#     def process_request(self, request):
#         print("Custom middle-ware process_request")
# 
#     def process_response(self, request, response):
#         print("Custom middle-ware process_response")
#         return response

    def  process_view(self, request, view_func, *view_args, **view_kwargs):
        """
        1. request is an HttpRequest object. 
        2. view_func is the Python function that Django is about to use.
        3. view_args is a list of positional arguments that will be passed to the view
        4. view_kwargs is a dictionary of keyword arguments that will be passed to the view.
         
        ## It should return either None or an HttpResponse object. 
        If it returns None, Django will continue processing this request, executing any other process_view() middleware and, 
        then, the appropriate view. If it returns an HttpResponse object, Django won't bother calling the appropriate view
        it will apply response middleware to that HttpResponse and return the result
        """
        print("Custom middle-ware process_view")
        return None
 
    def process_template_response(self, request, response):
        print("Custom middle-ware process__template_response")
        return response
 
    def process_exception(self, request, exception):
        """
        1. request is an HttpRequest object. 
        2. exception is an Exception object raised by the view function.
         
        Django calls process_exception() when a view raises an exception. 
        ## process_exception() should return either None or an HttpResponse object. 
        If it returns an HttpResponse object, the template response and response middleware will be applied and 
        the resulting response returned to the browser. Otherwise, default exception handling kicks in.
         
        Again, middleware are run in reverse order during the response phase, which includes process_exception. 
        If an exception middleware returns a response, the process_exception methods of the middleware classes
        above that middleware won't be called at all.
        """
        print("Custom middle-ware process_exception")
        return None