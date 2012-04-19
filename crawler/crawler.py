"""
Hackingpot crawler

Developed by Gian Carlo d'Orleans-Brissac Cecilio Martinelli on 2012-04-14.
Licensed under Creative Commons BY-NC-SA

"""

import urllib2
import time
import pickle
from BeautifulSoup import BeautifulSoup

#initial crawl targets
targets = [['http://makeprojects.com/c/Arduino', 0],
			['http://makeprojects.com/c/Audio', 0],
			['http://makeprojects.com/c/Circuits', 0],
			['http://makeprojects.com/c/Computers', 0],
			['http://makeprojects.com/c/Hacks_and_Mods',0],
			['http://makeprojects.com/c/Ham_Radio', 0],
			['http://makeprojects.com/c/Microcontrollers', 0],
			['http://makeprojects.com/c/Motors', 0],
			['http://makeprojects.com/c/Musical_Instruments',0],
			['http://makeprojects.com/c/Open_Source_Hardware',0],
			['http://makeprojects.com/c/Open_Source_Software',0],
			['http://makeprojects.com/c/Programming',0],
			['http://makeprojects.com/c/Repurposed_Tech',0],
			['http://makeprojects.com/c/Soft_Circuits',0],
			['http://makeprojects.com/c/Soldering',0],
			['http://makeprojects.com/c/Wireless',0],
			]
#sources crawler is allowed to search
sources = ['http://makeprojects.com',
			'http://www.makeprojects.com',
			'/Project/']

#crawler depth search limit
depth_limit = 1

def crawl_web(seed):
	tocrawl = seed
	crawled = []
	part_index = {}
	project_index = {}
	while tocrawl:
		target = tocrawl.pop()
		page = target[0]
		page_depth = target[1]
		if page not in crawled:
			if page_depth <= depth_limit:
				#only crawl pages inside allowed websites
				if is_allowed_link(page, sources) == True:
					print 'crawling: ', page
					depth = page_depth
					content = get_page(page)
					add_part_index(part_index, content, page)
					add_project_index(project_index, content, page)
					outlinks = get_all_links(content)
					for link in outlinks:
						if link.find('http://') != -1 or link.find('www') != -1:
							tocrawl.append([link, depth+1])
						else:
							corrected_link = sources[0]+link
							tocrawl.append([corrected_link, depth+1])
					crawled.append(page)
	#pickle dictionaries for later queries - addresses are different when in production server.
	pickle.dump(part_index, open("../part_index.p", "wb"))
	pickle.dump(project_index, open("../project_index.p", "wb"))
	return part_index, project_index
	
def get_page(url):
	try: 
		response = urllib2.urlopen(url)
	except:
		return ""
	return response.read()
	
def get_all_links(page):
	res = []
	soup = BeautifulSoup(page)
	links = soup.findAll('a')
	for link in links:
		try:
			res.append(str(link['href']))			
		except KeyError:
			pass
	return res

def add_part_index(part_index, content, url):
	if url.find('/Project/') != -1:
		if find_details(content) == None:
			return None
		parts, project, image = find_details(content)
		for part in parts:
			add_to_part_index(part_index, part, project)
		
def add_to_part_index(part_index, part, project):
	if part in part_index:
		if project not in part_index[part]:
			part_index[part].append(project)
	else:
		part_index[part] = [project]

def add_project_index(project_index, content, url):
	if url.find('/Project/') != -1:
		if find_details(content) == None:
			return None
		parts, project, image = find_details(content)
		add_to_project_index(project_index, project, parts, image, url)

def add_to_project_index(project_index, project, parts, image, url):
	project_index[project] = [parts, image, url]

#part_index structure:
#{'Part name': [project1, project2, ...]}
#project_index structure:
#{'Project': [[part1, part2, ...], images, url], ...}

def find_details(content):
	parts = []
	soup = BeautifulSoup(content)
	parts_soup = soup.findAll("ul", {"data-itemtype":"part"})
	for column in parts_soup:
		part_links = column.findAll("a", {"class":"itemName muted"})
		for part in part_links:
			#make 'part' lower-case so later, in search, it is case insensitive
			part = str(part.text).lower()
			parts.append(part)
	try:
		project = str(soup.h1.text)
		image = str(soup.find(id="guideWikiDetails").img['src'])
	except AttributeError:
		print 'no image found on'
		return None
	return parts, project, image

def is_allowed_link(link, sources=""):
	#if link resides inside Make Projects, return True
	flag = False
	for source in sources:
		if link.find(source) != -1:
			flag = True
	if sources == "":
		flag = True
	return flag
