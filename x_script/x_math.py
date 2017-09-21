#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :x_math.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


from collections import Counter

import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm


class XMath(object):
	"""the XMath class"""
	def __init__(self):
		"""
		@the XMath class initialization
		"""

	def addTwoPointDict(self,dict1,dict2):
		"""
		@add two point dict
		"""
		return Counter(dict1) + Counter(dict2)


if __name__ == "__main__":

	p = XMath()
	p.addTwoPointDict({"a":1},{"a":2,"b":3})
