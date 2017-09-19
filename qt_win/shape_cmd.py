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

from x_script.x_blendShape import XBlendShape 


class ShapeCmd(object):

	def __init__(self):

		self.blendShape = XBlendShape()

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


	def test(self):

		print "shape cmd test"


if __name__ == "__main__":
	p = ShapeCmd()
	p.getBlendShapeInfo()