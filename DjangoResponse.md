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

from rest_framework import status
from rest_framework.response import Response
Response(None, status=status.HTTP_400_BAD_REQUEST)