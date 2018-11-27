#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
#
# @name   : E-ntel - Email Information Gathering
# @url    : http://github.com/CybernetiX-S3C
# @author : John Modica (CybernetiX S3C)

from lib.output import *
from lib.request import *
from lib.parser import *

class Yahoo(Request):
	def __init__(self,target):
		Request.__init__(self)
		self.target = target

	def search(self):
		test('Searching "%s" in Yahoo...'%(self.target))
		url = "http://search.yahoo.com/search?p=%40{target}&b=0&pz=10".format(
			target=self.target)
		try:
			resp = self.send(
				method = 'GET',
				url = url,
				headers = {
							'Host':'search.yahoo.com'
				}
				)
			return self.getemail(resp.content,self.target)
		except Exception as e:
			pass

	def getemail(self,content,target):
		return parser(content,target).email()