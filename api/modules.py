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
	before_title = "<title>"
	after_title = "</title>"
	before_direct_link = '<a class="preview_thumb" href="'
	after_direct_link = '.mp4'
	
	mobile_link = link.replace("www", "m")
	#transforming desktop link to mobile link
	try:
		page = urlopen(mobile_link).read()
	except (IOError):
		return 1
	#loading the page
	
	title = page[page.find(before_title)+len(before_title):page.find(after_title)]
	#getting the title of the video
	video_link = page[page.find(before_direct_link)+len(before_direct_link):page.find(after_direct_link)+len(after_direct_link)]
	#getting the direct link to the video
	
	return [title, video_link]

