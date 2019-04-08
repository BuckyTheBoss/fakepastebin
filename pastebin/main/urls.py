from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   path('snippet/<int:snippet_id>', views.snippet, name='snippet'),
   path('snippet/addurlsnippet', views.add_url_snippet, name='add_url_snippet'),
   path('snippet/addtextsnippet', views.add_text_snippet, name='add_text_snippet'),
   path('search', views.search, name='search'),
   path('login', auth_views.LoginView.as_view(), name='login')
]
