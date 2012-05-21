from searchengine import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
	query = request.GET.get('q', '')
	query = query.strip()
	q = []
	if query:
		query = query.split(',')
		for entry in query:
			s = entry.lower()
			q.append(s)
		results = searchquery(q)
		return render_to_response('search.html', dict(results=results, query=query))
	return render_to_response('search.html', dict(results=None, query=None))