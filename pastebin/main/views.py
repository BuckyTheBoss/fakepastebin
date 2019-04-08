from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q


# Create your views here.
def index(request):
	all_snippets = Snippet.objects.all().order_by('-pub_date')
	print(dir(request.session))
	print(request.session.values())
	return render(request, 'index.html', {'all_snippets' : all_snippets})

def snippet(request,snippet_id):
	snippet = Snippet.objects.get(pk=snippet_id)
	snippet.views += 1
	snippet.save()
	return render(request, 'snippet.html', {'snippet' : snippet})

def add_url_snippet(request):
	if request.method == 'POST':
		url_snippet = UrlSnippetForm(request.POST)
		url_snippet.save()
		return redirect('index')
	form = UrlSnippetForm()
	return render(request, 'addsnippet.html',{'form' : form})

def add_text_snippet(request):
	if request.method == 'POST':
		url_snippet = TextSnippetForm(request.POST)
		url_snippet.save()
		return redirect('index')
	form = TextSnippetForm()
	return render(request, 'addsnippet.html',{'form' : form})

def search(request):
	if request.method != 'POST':
		return redirect('index')

	text = request.POST.get('search', '')
	results = Snippet.objects.filter(
		Q(urlsnippet__content__icontains=text) |
		Q(textsnippet__content__icontains=text) )

	return render(request, 'search_results.html', {'results' : results, 'text' : text})