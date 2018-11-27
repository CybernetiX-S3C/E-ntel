#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
#
# @name   : E-ntel - Email Information Gathering
# @url    : http://github.com/CybernetiX-S3C
# @author : John Modica (CybernetiX S3C)

from json import loads
from lib.output import *
from lib.request import *
from lib.parser import *

class Pwned(Request):
	def __init__(self,email):
		Request.__init__(self)
		self.email = email

	def search(self):
		url = "https://hacked-emails.com/api?q={email}".format(
			email=self.email)
		try:
			resp = self.send(
				method = 'GET',
				url = url
				)
			if resp.status_code == 200:
				return loads(resp.content)
		except Exception as e:
			pass