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

	def getObjectBoundingBox(self,obj,mode=0):
		"""
		@get the given object bounding box
		"""
		obj = self.getTransformNode(obj)
		if obj:
			xmin,ymin,zmin,xmax,ymax,zmax = mc.xform(obj,q=True,boundingBox=True)
		if mode == 1:
			yWeight = ymax - ymin
			return yWeight
		elif mode == 2:
			zWeight = zmax - zmin
			return zWeight
		else:
			xWeight = xmax - xmin
			return xWeight

	def getTransformNode(self,obj):
		"""
		@get the given object tranfrom node
		"""
		if not obj:
			return
		if not mc.objExists(obj):
			return
		objType = mc.objectType(obj)
		if objType in ["mesh","nurbsSurface","nurbsCurve","lattice"]:
			obj = mc.listRelatives(obj,p=True,f=True)[0]
		objType = mc.objectType(obj)
		if objType == "transform":
			return obj

	def getIntermediateShape(self,node):
		"""
		@get the intermediate shape
		"""
		node = self.getTransformNode(node)
		shapes = mc.listRelatives(node,s=True,f=True)
		if shapes:
			for shape in shapes:
				if mc.getAttr("%s.intermediateObject" %shape):
					return shape

	def getObjShape(self,node):
		"""
		@get object shape
		"""
		node = self.getTransformNode(node)
		shapes = mc.listRelatives(node,s=True,f=True,ni=True)
		if shapes:
			return shapes[0]

	def duplicateObject(self,obj,name):
		"""
		@duplicate the given object and rename it
		"""
		obj = self.getTransformNode(obj)
		dupObj = mc.duplicate(obj,n=name)
		if dupObj:
			dupObj = dupObj[0]
			interShape = self.getIntermediateShape(dupObj)
			mc.delete(interShape)
		return dupObj

if __name__ == "__main__":

	f = XObject()
	print f.getObjectInputs("pSphere1","skinCluster")
