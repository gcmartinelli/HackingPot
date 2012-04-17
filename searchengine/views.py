from searchengine import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
	query = request.GET.get('q', '').split()
	results = searchquery(query)
	return render_to_response('search.html', dict(results=results, query=query))