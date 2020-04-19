from django.contrib import admin

from .models import Snippet, Blog, Entry, Author

admin.site.register(Snippet)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)