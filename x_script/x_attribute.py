#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :x_attribute.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm


class XAttribute(object):

	def __init__(self):

		pass

	def quickUnLockObjAttr(self,obj,*args):
		"""
		@quick unlock given object attributs
		"""
		if not args:
			attrs = mc.listAttr(obj,keyable=True)
			for attr in attrs:
				mc.setAttr("%s.%s" %(obj,attr),lock=False)
		else:
			for attr in args:
				mc.setAttr("%s.%s" %(obj,attr),lock=False)

	def quickLockObjAttr(self,obj,*args):
		"""
		@quick lock object attributes
		"""
		if not args:
			attrs = mc.listAttr(obj,keyable=True)
			for attr in attrs:
				mc.setAttr("%s.%s" %(obj,attr),lock=True)
		else:
			for attr in args:
				mc.setAttr("%s.%s" %(obj,attr),lock=True)

	def test(self):

		pass


if __name__ == "__main__":

	p = XAttribute()
	p.quickUnLockObjAttr("blendShape1_pSphere2_5500_blsGeo")