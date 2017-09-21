#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :shape_cmd.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm

from x_script import x_blendShape
reload(x_blendShape)
from x_script import x_shape
reload(x_shape)
from x_script import x_object
reload(x_object)
from x_script import x_attribute
reload(x_attribute)
from x_script import x_math
reload(x_math)

from x_script.x_blendShape import XBlendShape
from x_script.x_shape import XShape
from x_script.x_object import XObject
from x_script.x_attribute import XAttribute
from x_script.x_math import XMath


class ShapeCmd(object):

	def __init__(self):

		self.blendShape = XBlendShape()
		self.shape = XShape()
		self.object = XObject()
		self.attribute = XAttribute()
		self.math = XMath()

	def getBlendShapeInfo(self):
		"""
		@get the blendShape information
		"""
		infos = {}
		nodes = self.blendShape.getBlendShapeNodes()
		if nodes:
			for node in nodes:
				infos[node] = {}
				trans = self.blendShape.getBlendShapeGeometry(node)
				for i,tran in enumerate(trans):
					infos[node][tran] = {}
					names = self.blendShape.getBlendShapeWeightName(node)
					for j,name in enumerate(names):
						weights = self.blendShape.getBlendShapeWeightValues(node,i,j)
						infos[node][tran][name] = weights
		return infos

	def linkOrNoBlendShapeTarget(self,texts,mode=True):
		"""
		@link blendShape target from given text
		"""
		if not texts:
			return
		if not isinstance(texts,list):
			texts = [texts]
		attrs = self.blendShape.getBlendShapeWeightAttrFromText(texts)
		if not attrs:
			return
		i = 1
		allDict = {}
		for attr in attrs:
			node,geoShape,weightName,weightValue = self.blendShape.fromAttrGetNameInfo(attr)
			parentNode = mc.listRelatives(geoShape,p=True,fullPath=True)[0]
			shapeOrg = self.object.getIntermediateShape(geoShape)
			if shapeOrg in allDict:
				orgPoints = allDict[shapeOrg]
			else:
				orgPoints = self.shape.getShapeVtxPosition(shapeOrg)
				allDict[shapeOrg] = orgPoints
			pmInTarget = pm.PyNode("%s.inputGeomTarget" %attr)
			if pmInTarget.isConnected():
				continue
			compPoints = self.blendShape.getBlendShapePointDict(attr)
			points = self.math.addTwoPointDict(orgPoints,compPoints)
			newObj = self.object.duplicateObject(geoShape,"%s_%s_%s_blsGeo" 
												%(node,weightName,weightValue))
			xValue = self.object.getObjectBoundingBox(geoShape)
			self.attribute.quickUnLockObjAttr(newObj)
			mc.setAttr("%s.tx" %newObj,xValue*i)
			self.shape.setShapeVtxPosition(newObj,points)
			if mode:
				pm.PyNode(newObj).outMesh.connect(pmInTarget)
			i += 1

	def exportBlendShapeTarget(self,texts):
		"""
		@export blendShape target
		"""
		if not texts:
			return
		if not isinstance(texts,list):
			texts = [texts]
		attrs = self.blendShape.getBlendShapeWeightAttrFromText(texts)
		if not attrs:
			return

	def test(self):

		print "shape cmd test"


if __name__ == "__main__":
	p = ShapeCmd()
	p.getBlendShapeInfo()