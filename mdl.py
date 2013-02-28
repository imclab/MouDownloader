#!/usr/bin/env python
# -*- coding: utf-8 -*-
#You need python 2.7.x , Download it from http://www.python.org

from sys import stdout, argv
from api.download import *
from api.modules import *

__version__ = "2.0"

__all__ = ("main")
__doc__ = '''
MouDownload

A Download tool.
This is the console version
'''


def main():
	"""
Example:
Pornhub/Youjizz/melodysheep/mixturecloud video link (don't forget http://): http://www.*****.com/view_video.php?viewkey=******
Getting link...
Found:
name_here
http://link_to_/video.mp4

Downloading video... this may take a while.
Download size	= 17735 ko, packet: 2166/2166
File name	= name_here.mp4
ETA		= 45 second(s)
md5 checksum	= 3fa1d9682acc09934d1e3ff0404eaf8e
File size	= 17735 kb
Saved in: /home/you/pyorn
Downloaded!
Press enter to continue...
"""
	try:
		if ("http://" in argv[1]):
			link = argv[1]
		else:
			print("This is not a valid link don't forget the 'http://'")
			return 1
	except (IndexError):
		link = raw_input("Enter mixturecloud/pornhub/youjizz/melodysheep link (don't forget http://): ")
	print("Getting link...")
	
	if ("pornhub" in link):
		print("pornhub detected")
		Flink = GetPornhubVideoLink(link)
	elif ("melodysheep" in link):
		Flink = GetMp3LinkFromMelodySheep(link)
	elif ("mixturecloud" in link):
		print("Mixturecloud detected")
		Flink = GetMixtureDirectLink(link)
		
	elif ("youjizz" in link):
		print("youjizz detected")
		Flink = GetYoujizzVideoLink(link)
	else:
		print("Incorrect link")
	
	if (Flink == 1):
		print("Check your internet connection or your link")
		return 1
	del link
	print("Found:\n%s\n%s\n\nDownloading file... this may take a while." % (Flink[0][:40], Flink[1]))
	try:
		download(Flink[1], Flink[0])
	except (IOError):
		return 1
	return 0

if __name__ == '__main__':
	if main():
		print("Oh noes errors happenned :(")
	else:
		print("Downloaded")
	raw_input("Press enter to continue...")
