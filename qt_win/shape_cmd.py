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

from x_script.x_blendShape import XBlendShape
from x_script.x_shape import XShape
from x_script.x_object import XObject 


class ShapeCmd(object):

	def __init__(self):

		self.blendShape = XBlendShape()
		self.shape = XShape()
		self.object = XObject()

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

	def linkBlendShapeTarget(self,texts):
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
		for attr in attrs:
			node,geo,name,weight = attr.split(".")
			idx = geo.split("[")[-1].split("]")[0]
			shape = mc.blendShape(node,q=True,geometry=True)[int(idx)]
			parentNode = mc.listRelatives(shape,p=True,fullPath=True)[0]
			shapeOrg = self.shape.getIntermediateShape(shape)
			pmInTarget = pm.PyNode("%s.inputGeomTarget" %attr)
			pmPoints = pm.PyNode("%s.inputPointsTarget" %attr)
			pmComps = pm.PyNode("%s.inputComponentsTarget" %attr)
			if pmInTarget.isConnected():
				continue





	def test(self):

		print "shape cmd test"


if __name__ == "__main__":
	p = ShapeCmd()
	p.getBlendShapeInfo()