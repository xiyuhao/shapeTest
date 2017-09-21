#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :x_json.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.8
##-----------------------------------------------------------

import json

import maya.cmds as mc
import maya.mel as  mel
import maya.OpenMaya as om
import pymel.core as pm


class XJson(object):
	"""the json data class"""

	def __init__(self):
		"""
		@set the json class initialization
		"""
		pass

	def writeJsonFile(self,data):
		"""
		@write the json data to given file
		"""
		jsonPath = mc.fileDialog2(fileFilter="*.json",dialogStyle=2,fileMode=0)
		if jsonPath:
			jsonPath = jsonPath[0]
			with open(jsonPath,"w") as jsonFile:
				jsonFile.write(json.dumps(data,indent=4))

	def readJsonFile(self):
		"""
		@read the json data from given file 
		"""
		jsonPath = mc.fileDialog2(fileFilter="*.json",dialogStyle=2,fileMode=1)
		if jsonPath:
			jsonPath = jsonPath[0]
			with open(jsonPath) as jsonFile:
				data = json.load(jsonFile)
				return data

if __name__ == "__main__":

	p = XJson()
	p.writeJsonFile({"a":1})