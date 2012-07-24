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

def GetPornhubVideoLink(link):
	'''Get the direct link to the video, return 1 if any errors
	don't forget the http://'''
	#definiting all variables for the next
	after_title = " - Pornhub.com</title>"
	before_title = "<title>"
	before_direct_link = 'class="play_video_link">\r\n            <div>\r\n                <a href="'
	after_direct_link = '" style="text'
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
	video_link = page[page.find(before_direct_link)+len(before_direct_link):page.find(after_direct_link)]
	return [real_title, video_link]

def GetYoujizzVideoLink(link):
	'''Get the direct link to the video, return 1 if any errors
	don't forget the http://'''
	before_video = '<div class="img">\r\n                \t<a href="'
	after_video = '" target="_self"><img'
	try:
		page = urlopen(link).read()
		#getting the page of the link
	except (IOError):
		return 1
	
	#searching the title
	before_title = "<title>"
	after_title = "</title>"
	real_title = page[page.find(before_title)+len(before_title):page.find(after_title)]
	if (not len(real_title)):
		#sometime the video page is loading with an empty title (searching the name again)
		before_title = '<h2 style="margin: 5px;">'
		after_title = '</h2>'
		real_title = page[page.find(before_title)+len(before_title):page.find(after_title)]
	#end of the search of the title of the video
	title = real_title.replace(" ", "%20")
	#during a search we need to replace ' ' with %20
	try:
		search = urlopen("http://m.youjizz.com/search/%s/page1.html" % title).read()
		#launch a search on the website
	except (IOError):
		return 1
	if ("mp4" not in search):
		return 1
	#directly search and return the direct link after the search
	video_link = search[search.find(before_video)+len(before_video):search.find(after_video)]
	return [real_title, video_link]
