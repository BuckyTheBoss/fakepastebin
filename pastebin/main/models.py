from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Snippet(models.Model):
	
	title = models.CharField(max_length=100, default='')
	pub_date = models.DateTimeField(default=timezone.now)
	views = models.IntegerField(default=0)
	author = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None, blank=True) #dont want it to cascade, look into replaceing with null

class UrlSnippet(Snippet):
	content = models.URLField()

class TextSnippet(Snippet):
	content = models.TextField()



class UrlSnippetForm(ModelForm):    
	class Meta:
		model = UrlSnippet
		fields = ['title', 'content']

class TextSnippetForm(ModelForm):    
	class Meta:
		model = TextSnippet
		fields = ['title', 'content']