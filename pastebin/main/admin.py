from django.contrib import admin
from .models import Snippet,UrlSnippet,TextSnippet

# Register your models here.
admin.site.register(Snippet)
admin.site.register(UrlSnippet)
admin.site.register(TextSnippet)