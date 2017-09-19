#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :x_blendShape.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm

from x_script import x_object
reload(x_object)

from x_script.x_object import XObject


class XBlendShape(object):
	"""the blendShape class"""
	def __init__(self):
		"""
		@blendShape class initialization
		"""
		self.object = XObject()

	def getBlendShapeNodes(self):
		"""
		@get all blendShape node from scene
		"""
		nodes = []
		sels = mc.ls(sl=True)
		if sels:
			for sel in sels:
				node = self.object.getObjectInputs(sel,"blendShape")
				if node:
					nodes.append(node)
		else:
			nodes = mc.ls(type="blendShape")
		return nodes

	def getBlendShapeWeightName(self,node):
		"""
		@get blendShape weight name
		"""
		names = []
		weights = mc.blendShape(node,q=True,weightCount=True)
		if weights:
			for weight in range(weights):
				name = mc.aliasAttr("%s.weight[%s]" %(node,weight),q=True)
				names.append(name)
		return names

	def getBlendShapeGeometry(self,node):
		"""
		@get blendShape geometry
		"""
		tranNodes = []
		shapes = mc.blendShape(node,q=True,geometry=True)
		if shapes:
			for shape in shapes:
				tranNode = mc.listRelatives(shape,p=True)
				if tranNode:
					tranNodes.append(tranNode[0])
		return tranNodes

	def getBlendShapeWeightValues(self,node,shapeItem,weightItem):
		"""
		@get blendShape weight item values
		"""
		weights = []
		nums = mc.getAttr(
				"%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem" 
				%(node,shapeItem,weightItem),multiIndices=True)
		for num in nums:
			newNum = (num - 5000.0) / 1000
			weights.append(newNum)
		return weights 

if __name__ == "__main__":

	p = XBlendShape()
	s = p.getBlendShapeNodes()
	print s