#!/usr/bin/env python
# -*- coding: utf-8 -*-
#this UI version is beta, use console version instead
#You need python 2.7.x , Download it from http://www.python.org
import wx#YOU MUST INSTALL WXPYTHON @ http://wxpython.org/download.php
import string
from urllib import urlopen
from api.modules import *
from api.download import *

__doc__ = '''
MouDownload

A Download tool
this is the GUI version
'''



class MyFrame(wx.Frame):
	def __init__(self, *args, **kwds):
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.label_1 = wx.StaticText(self, -1, "Enter bandcamp/pornhub/mixturecloud/youjizz video link :")
		self.output = wx.StaticText(self, -1, "")
		self.xinput = wx.TextCtrl(self, -1, "")
		self.enter = wx.Button(self, -1, "Download!")
		self.__set_properties()
		self.__do_layout()
		self.Bind(wx.EVT_TEXT, self.ainput, self.xinput)
		self.Bind(wx.EVT_BUTTON, self.download, self.enter)

	def __set_properties(self):
		self.SetTitle("FreeDownloader")
		self.output.SetLabel("Wait if its not responding")

	def __do_layout(self):
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		grid_sizer_1 = wx.GridSizer(2, 1, 0, 0)
		grid_sizer_2 = wx.GridSizer(1, 2, 0, 0)
		grid_sizer_3 = wx.GridSizer(2, 1, 0, 0)
		grid_sizer_3.Add(self.label_1, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
		grid_sizer_3.Add(self.output, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
		grid_sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
		grid_sizer_2.Add(self.xinput, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
		grid_sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
		grid_sizer_1.Add(self.enter, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
		sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()

	def ainput(self, event):
		event.Skip()

	def download(self, event):
		try:
			link = self.xinput.GetValue()
			if ("pornhub" in link):
				Flink = GetPornhubVideoLink(link)
			elif ("youjizz" in link):
				Flink = GetYoujizzVideoLink(link)
			elif ("bandcamp" in link):
				Flink = GetMp3LinkFromBandCamp(link)
			elif ("mixturecloud" in link):
				Flink = GetMixtureDirectLink(link)
			else:
				print("Incorrect link")
			download(Flink[1], Flink[0])
			self.output.SetLabel("Downloaded! : %s" % Flink[0])
		except:
			self.output.SetLabel("Error, check the link or the internet connection")
		event.Skip()


if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()
