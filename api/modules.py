#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
from urllib import urlopen

__doc__ = """
MouDownload

All modules are defined here
To add a module just create a function which
return a list like this: [name_of_video, direct_link_to_video]
"""

def search(list, str):
	'''searching a string in a list'''
	for item in list:
		if (str in item):
			return item
	return ''

def GetPornhubVideoLink(link):
	'''Get the direct link to the video, return 1 if any errors
	don't forget the http://'''
	#definiting all variables for the next
	after_title = " - Pornhub.com</title>"
	before_title = "<title>"
	video_type = 'mp4'
	
	table = string.maketrans(" &-!@?", "_"*6)
	#on video link all specials chars are replaced with '_'
	try:
		viewkey = link.split("=")[1]
		#getting view key
		page = urlopen(link).read()
	except (IOError, IndexError):
		return 1
	real_title = page[page.find(before_title)+len(before_title):page.find(after_title)]
	#getting the video title
	title = real_title.translate(table)
	try:
		page = urlopen("http://m.pornhub.com/video/show/title/%s/vkey/%s" % (title, viewkey)).read()
		#loading the mobile version of the video
	except (IOError):
		return 1
	#searching the direct link of the video and return it
	video_link = search(page.split('"'), video_type)
	return [real_title, video_link]

def GetYoujizzVideoLink(link):
	'''Get the direct link to the video, return 1 if any errors
	don't forget the http://'''
	before_title = "<title>"
	after_title = "</title>"
	video_type = 'mp4'
	
	mobile_link = link.replace("www", "m")
	#transforming desktop link to mobile link
	try:
		page = urlopen(mobile_link).read()
	except (IOError):
		return 1
	
	title = page[page.find(before_title)+len(before_title):page.find(after_title)]
	video_link = search(page.split('"'), video_type)
	
	return [title, video_link]

