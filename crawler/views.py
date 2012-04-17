"""
Hackingpot crawler

Developed by Gian Carlo d'Orleans-Brissac Cecilio Martinelli on 2012-04-14.
Licensed under Creative Commons BY-NC-SA

"""
from crawler import *
from django.http import HttpResponse

def crawl(request):
	part_index, project_index = crawl_web(targets)
	response = "%s projects crawled." % len(project_index)
	return HttpResponse(response)