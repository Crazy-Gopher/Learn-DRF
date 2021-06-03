from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect


## HttpResponse(content=b'', content_type=None, status=200, reason=None, charset=None)
content = "Here's the text of the Web page." or "<h1>Here's the text of the Web page.</h1>"
or json.dumps({'status_code': 'USER_NOT_REGISTERED'})

JsonResponse(data = serializer.data, status=200)

Telling the browser to treat the response as a file attachment
response = HttpResponse(my_data, content_type='application/vnd.ms-excel')
response['Content-Disposition'] = 'attachment; filename="foo.xls"'

## render_to_response(template_name, context=None, content_type=None, status=None, using=None):
render(request, template_name, context=None, content_type=None, status=None, using=None):
redirect(to, *args, permanent=False, **kwargs):

render(request, 'myapp/index.html', {'foo': 'bar',}, content_type='application/xhtml+xml')

reverse
200 400 401 403 405 500

## HttpRequest
self.body
self.GET = QueryDict(mutable=True)
self.POST = QueryDict(mutable=True)
self.COOKIES = {}
self.META = {}
self.FILES = MultiValueDict()

self.path = ''
self.path_info = ''
self.method = None
self.resolver_match = None
self.content_type = None
self.content_params = None


## Django restframework

# Request
request.data: flexible parcing, it can parse json, xml data similar to form data. request.POST and request.FILES
request.query_params: it is used to get query parameter. request.GET
request.user: request.user typically returns an instance of django.contrib.auth.models.User, although the behavior depends on the authentication policy being used.
    If the request is unauthenticated the default value of request.user is an instance of django.contrib.auth.models.AnonymousUser.
request.auth: 

# Response:
Response class simply provides a nicer interface for returning content-negotiated Web API responses, that can be rendered to multiple formats.
Unless you want to heavily customize REST framework for some reason, you should always use an APIView class or @api_view function for views that return Response objects.
Doing so ensures that the view can perform content negotiation and select the appropriate renderer for the response, before it is returned from the view.


from rest_framework import status
from rest_framework.response import Response
Response(data, status=None, template_name=None, headers=None, content_type=None)
Response(None, status=status.HTTP_400_BAD_REQUEST)

Arguments:

data: The serialized data for the response.
status: A status code for the response. Defaults to 200. See also status codes.
template_name: A template name to use if HTMLRenderer is selected.
headers: A dictionary of HTTP headers to use in the response.
content_type: The content type of the response. Typically, this will be set automatically by the renderer as determined by content negotiation, but there may 
  be some cases where you need to specify the content type explicitly.
