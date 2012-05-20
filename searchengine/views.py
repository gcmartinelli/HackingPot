from searchengine import *
from django.http import HttpResponse
from django.shortcuts import render_to_response

def search(request):
	query = request.GET.get('q', '')
	query = query.split(',')
	q = []
	for entry in query:
		l = len(entry)
		i = 0
		if l > 0:
			while i < l:
				if entry[i] == " ":
					i += 1
			if i == l:
				results = None
				query = None
				return render_to_response('search.html', dict(results=results, query=query))
			while entry[0] == " ":
				entry = entry[1:]
			s = entry.lower()
			q.append(s)
		results = None
		query = None
		return render_to_response('search.html', dict(results=results, query=query))
	results = searchquery(s)
	return render_to_response('search.html', dict(results=results, query=query))




#def search(request):
#	query = request.GET.get('q', '')
#	if len(query) > 0 and query != " ":
#		query = query.split(',')
#		q = []
#		for entry in query:
#			s = entry.lower()
#			while s[0] == " ":
#				s = s[1:]
#			q.append(s)
#		results = searchquery(q)
#		return render_to_response('search.html', dict(results=results, query=query))
#	else:
#		results = None
#		return render_to_response('search.html', dict(results=results, query=query))