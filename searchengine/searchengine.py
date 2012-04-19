"""
Hackingpot search

Developed by Gian Carlo d'Orleans-Brissac Cecilio Martinelli on 2012-04-14.
Licensed under Creative Commons BY-NC-SA

"""

import pickle 
import operator

def searchquery(query):
	query_lower = []
	#turn search query into lower-case query
	for q in query:
		query_lower.append(q.lower())
	results = []
	queryresults = lookup(query_lower)
	if queryresults == []:
		return None
	rank = ranking(query_lower, queryresults)
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
		#pickle dictionaries for later queries - addresses are different when in production server.
		part_index = pickle.load(open("../part_index.p", "rb"))
		try:
			for project in part_index[part]:
				if project not in results:
					results.append(project)
		except KeyError:
			return results
	return results
	
def ranking(query, queryresults):
	#pickle dictionaries for later queries - addresses are different when in production server.
	project_index = pickle.load(open("../project_index.p", "rb"))
	ranking = []
	for project in queryresults:
		count = 0
		for part in project_index[project][0]:
			for querypart in query:
				if querypart == part:
					count += 1.0
		rank = count/len(project_index[project][0])
		ranking.append([project, rank])
	return ranking
	
def project_details(projectname):
	#pickle dictionaries for later queries - addresses are different when in production server.
	project_index = pickle.load(open("../project_index.p", "rb"))
	parts = project_index[projectname][0]
	image = project_index[projectname][1]
	url = project_index[projectname][2]
	return parts, image, url
