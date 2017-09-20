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

from x_script.x_blendShape import XBlendShape
from x_script.x_shape import XShape
from x_script.x_object import XObject
from x_script.x_attribute import XAttribute 


class ShapeCmd(object):

	def __init__(self):

		self.blendShape = XBlendShape()
		self.shape = XShape()
		self.object = XObject()
		self.attribute = XAttribute()

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
			geoIdx = geo.split("[")[-1].split("]")[0]
			shape = mc.blendShape(node,q=True,geometry=True)[int(geoIdx)]
			weightNames = self.blendShape.getBlendShapeWeightName(node)
			nameIdx = name.split("[")[-1].split("]")[0]
			weightName = weightNames[int(nameIdx)]
			newWeight = weight.split("[")[-1].split("]")[0]
			parentNode = mc.listRelatives(shape,p=True,fullPath=True)[0]
			shapeOrg = self.object.getIntermediateShape(shape)
			pmOrg = pm.PyNode(shapeOrg)
			pmInTarget = pm.PyNode("%s.inputGeomTarget" %attr)
			pmPoints = pm.PyNode("%s.inputPointsTarget" %attr)
			pmComps = pm.PyNode("%s.inputComponentsTarget" %attr)
			if pmInTarget.isConnected():
				continue
			newObj = self.object.duplicateObject(shape,"%s_%s_%s_blsGeo" 
												%(node,weightName,newWeight))
			newShape = self.object.getObjShape(newObj)
			newShape = pm.PyNode(newShape)
			xValue = self.object.getObjectBoundingBox(shape)
			self.attribute.quickUnLockObjAttr(newObj)
			mc.setAttr("%s.tx" %newObj,xValue*i)
			points = []
			print pmOrg
			for vtx in pmOrg.vtx:
				point = vtx.getPosition()
				points.append(point)
			compsVtx = pmComps.get()
			compsPoint = pmPoints.get()
			if compsVtx:
				j = 0
				for compVtx in compsVtx:
					compVtx = pm.general.MeshVertex("%s.%s" %(shapeOrg,compVtx))
					for vtx in compVtx:
						vIdx = vtx.split("[")[-1].split("]")[0]
						points[int(vIdx)] = points[int(vIdx)] + compsPoint[j]
						j += 1
			for n,nVtx in enumerate(newShape.vtx):	
				nVtx.setPosition(points[n])
			newShape.outMesh.connect(pmInTarget)
			i += 1

	def test(self):

		print "shape cmd test"


if __name__ == "__main__":
	p = ShapeCmd()
	p.getBlendShapeInfo()