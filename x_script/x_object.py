#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :x_object.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm


class XObject(object):
	"""the object class"""
	def __init__(self):
		"""
		@the xobject class initialization
		"""
		pass

	def getObjectInputs(self,obj,type):
		"""
		@get the object given type node name
		"""
		allInputs = mc.listHistory(obj,pruneDagObjects=True)
		if allInputs:
			for input in allInputs:
				if mc.nodeType(input) == type:
					return input

