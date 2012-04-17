"""
Hackingpot search

Developed by Gian Carlo d'Orleans-Brissac Cecilio Martinelli on 2012-04-14.
Licensed under Creative Commons BY-NC-SA

"""

import pickle 
import operator

def lookup(query):
	results = []
	for part in query:
		part_index = pickle.load(open("part_index.p", "rb"))
		try:
			for project in part_index[part]:
				if project not in results:
					results.append(project)
		except KeyError:
			return results
	return results
	
def ranking(query, queryresults):
	project_index = pickle.load(open("project_index.p", "rb"))
	ranking = []
	for project in queryresults:
		count = 0
		for part in project_index[project][0]:
			for querypart in query:
				if querypart == part:
					count += 1.0
		print count
		rank = count/len(project_index[project][0])
		ranking.append([project, rank])
	return ranking
	
def searchquery(query):
	results = []
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
	
def project_details(projectname):
	project_index = pickle.load(open("project_index.p", "rb"))
	parts = project_index[projectname][0]
	image = project_index[projectname][1]
	url = project_index[projectname][2]
	return parts, image, url