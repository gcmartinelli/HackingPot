from searchengine import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
	query = request.GET.get('q', '')
	print query
	query = query.split(',')
	q = []
	for entry in query:
		s = entry.lower()
		while s[0] == " ":
			s = s[1:]
		q.append(s)
	results = searchquery(q)
	return render_to_response('search.html', dict(results=results, query=query))