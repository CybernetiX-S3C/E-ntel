#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
#
# @name   : E-ntel - Email Information Gathering
# @url    : http://github.com/CybernetiX-S3C
# @author : John Modica (CybernetiX S3C)

import re

class parser:
	def __init__(self,content,target):
		self.target = target
		self.content = str(content)

	def email(self):
		tmp_email = re.findall(r'[a-zA-Z0-9.\-_+#~!$&\',;=:]+'
			+'@'+r'[a-zA-Z0-9.-]*'+self.target,self.clean)
		email_list = []
		for _ in tmp_email:
			if _ not in email_list:
				email_list.append(_)
		return email_list

	@property
	def clean(self):
		self.content = re.sub('<em>','',self.content)
		self.content = re.sub('<b>','',self.content)
		self.content = re.sub('</b>','',self.content)
		self.content = re.sub('</em>','',self.content)
		self.content = re.sub('<strong>','',self.content)
		self.content = re.sub('</strong>','',self.content)
		self.content = re.sub('<wbr>','',self.content)
		self.content = re.sub('</wbr>','',self.content)
		for x in ('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C'):
			self.content = self.content.replace(x,' ')
		return self.content
