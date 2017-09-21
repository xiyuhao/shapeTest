#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :x_shape.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm


class XShape(object):
	"""the XShape class"""

	def __init__(self):
		"""
		@the XShape class initialization
		"""
		pass

	def getShapeType(self,name):
		"""
		@get shape type
		"""
		if not mc.objExists(name):
			return
		node = pm.PyNode(name)
		if node.type() == "transform":
			node = node.getShape()
		return node.type()

	def getShapeVtxPosition(self,name,space="preTransform"):
		"""
		@get the given shape vertex position
		"""
		points = {}
		if self.getShapeType(name) == "mesh":
			node = pm.PyNode(name)
			for vtx in node.vtx:
				idx = vtx.split(".")[-1]
				point = vtx.getPosition(space)
				points[idx] = point
		return points

	def setShapeVtxPosition(self,name,points={},space="preTransform"):
		"""
		@set the given shape vertex position
		"""
		if self.getShapeType(name) != "mesh":
			return
		node = pm.PyNode(name)
		for vtx in node.vtx:
			idx = vtx.split(".")[-1]
			if idx in points:
				vtx.setPosition(points[idx],space)

	def addShapeVtxPosition(self,orgName,dstName,points={},space="preTransform"):
		"""
		@add the shape vertex position
		"""
		orgPoints = self.getShapeVtxPosition(orgName,space)
		for vtx in orgPoints:
			if vtx in points:
				orgPoints[vtx] = orgPoints[vtx] + points[vtx]
		self.setShapeVtxPosition(dstName,orgPoints,space)

	def test(self):

		pass


if __name__ == "__main__":

	p = XShape()
	f = p.getShapeVtxPosition("pSphere1")
	b = p.getShapeVtxPosition("pSphere2")