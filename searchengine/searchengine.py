"""
Hackingpot search

Developed by Gian Carlo d'Orleans-Brissac Cecilio Martinelli on 2012-04-14.
Licensed under Creative Commons BY-NC-SA

"""

from mainapp.models import Project, Part
import operator
from django.core.exceptions import ObjectDoesNotExist

def searchquery(query):
	results = []
	print 'searchquery: ', query
	queryresults = lookup(query)
	if queryresults == []:
		return None
	rank = ranking(query, queryresults)
	for project in rank:
		pname = project[0]
		prank = project[1]*100
		parts, image, url = project_details(pname)
		results.append([pname, prank, parts, image, url])
	results.sort(key=operator.itemgetter(1), reverse=True)
	return results

def lookup(query):
	results = []
	for part in query:
		try:
			proj = Project.objects.filter(parts__name__icontains=part)
			for p in proj:
				if p.name not in results:
					results.append(str(p.name))
		except Project.DoesNotExist:
			pass
	return results

def ranking(query, queryresults):
	ranking = []
	for project in queryresults:
		count = 0
		proj = Project.objects.get(name=project)
		parts = proj.parts.all()
		for part in parts:
			for querypart in query:
				#if querypart == part:
				if str(part).find(querypart) != -1:
					count += 1.0
		rank = count/len(parts)
		ranking.append([project, rank])
	print ranking
	return ranking
	
def project_details(projectname):
	proj = Project.objects.get(name=projectname)
	parts = proj.parts.all()
	image = proj.image
	url = proj.url
	return parts, image, url