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
from x_script import x_skin
reload(x_skin)

from x_script.x_blendShape import XBlendShape
from x_script.x_shape import XShape
from x_script.x_object import XObject
from x_script.x_attribute import XAttribute
from x_script.x_math import XMath
from x_script.x_skin import XSkin


class ShapeCmd(object):

	def __init__(self):

		self.blendShape = XBlendShape()
		self.shape = XShape()
		self.object = XObject()
		self.attribute = XAttribute()
		self.math = XMath()
		self.skin = XSkin()

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

	def createSplitShapeNode(self,sculptMesh,orgMesh,skinMesh,outMesh):
		"""
		@create the split shape node
		"""
		sculptShape = self.object.getObjShape(sculptMesh)
		if mc.objectType(sculptShape) != "mesh":
			return
		orgShape = self.object.getObjShape(orgMesh)
		if mc.objectType(orgShape) != "mesh":
			return
		skinShape = self.object.getObjShape(skinMesh)
		if mc.objectType(skinShape) != "mesh":
			return
		skinNode = self.object.getObjectInputs(skinShape,"skinCluster")
		if not skinNode:
			return
		outShape = self.object.getObjShape(outMesh)
		if mc.objectType(outShape) != "mesh":
			return
		if mc.polyCompare(orgShape,sculptShape,e=True):
			return
		if mc.polyCompare(orgShape,skinShape,e=True):
			return
		if mc.polyCompare(orgShape,outShape,e=True):
			return
		splitShapeNode = mc.deformer(outMesh,
									type="splitShapeNode",
									n="%s_splitShapeNode" %outMesh)
		if not splitShapeNode:
			return
		splitShapeNode = splitShapeNode[0]
		infNames = self.skin.getSkinInfs(skinNode)
		mc.connectAttr("%s.outMesh" %orgShape,"%s.orgMesh" %splitShapeNode)
		mc.connectAttr("%s.outMesh" %sculptShape,"%s.sculptMesh" %splitShapeNode)
		mc.connectAttr("%s.wtDrty" %skinNode,"%s.skinWeight" %splitShapeNode)
		for i,inf in enumerate(infNames):
			mc.setAttr("%s.weightInputs[%s]" %(splitShapeNode,i),0)
			mc.aliasAttr(inf,"%s.weightInputs[%s]" %(splitShapeNode,i))

	def getSplitShapeOuts(self,splitMesh,tz=0.0):
		"""
		@get split shape output geos
		"""
		splitOutGrp = "split_Shape_out_grp"
		if not mc.objExists(splitOutGrp):
			splitOutGrp = mc.createNode("transform",n=splitOutGrp)
		splitNode = self.object.getObjectInputs(splitMesh,"splitShapeNode")
		if not splitNode:
			return
		nums = mc.getAttr("%s.weightInputs" %splitNode,multiIndices=True)
		if not nums:
			return
		for num in nums:
			mc.setAttr("%s.weightInputs[%s]" %(splitNode,int(num)),0)
		sculptShape = mc.listConnections("%s.sculptMesh" %splitNode,s=True,d=False)
		if sculptShape:
			sculptShape = sculptShape[0]
		else:
			return
		orgShape = mc.listConnections("%s.orgMesh" %splitNode,s=True,d=False)
		if not orgShape:
			return
		skinWeight = mc.listConnections("%s.skinWeight" %splitNode,s=True,d=False)
		if not skinWeight:
			return
		xWeight = self.object.getObjectBoundingBox(splitMesh)
		tt = mc.getAttr("%s.t" %splitMesh)[0]
		print tt
		for i,num in enumerate(nums):
			aliasName = mc.aliasAttr("%s.weightInputs[%s]" %(splitNode,int(num)),q=True)
			name = "%s_%s_splitShape_outMesh" %(sculptShape,aliasName)
			if mc.objExists(name):
				continue
			else:
				mc.setAttr("%s.weightInputs[%s]" %(splitNode,int(num)),1)
				dupObj = mc.duplicate(splitMesh,n=name)[0]
				mc.setAttr("%s.tx" %dupObj,tt[0] + (i+1)*xWeight)
				mc.setAttr("%s.tz" %dupObj,tt[2] + tz)
				mc.parent(dupObj,splitOutGrp)
				mc.setAttr("%s.weightInputs[%s]" %(splitNode,int(num)),0)

	def batchGetSplitShapeOuts(self,sels):
		"""
		@batch get split shape output geos
		"""
		splitMesh = sels.pop(-1)
		splitNode = self.object.getObjectInputs(splitMesh,"splitShapeNode")
		if not splitNode:
			return
		self.getSplitShapeOuts(splitMesh,0.0)
		zWeight = self.object.getObjectBoundingBox(splitMesh,2)
		if len(sels) > 0:
			for i,sel in enumerate(sels):
				selShape = self.object.getObjShape(sel)
				mc.connectAttr("%s.outMesh" %selShape,"%s.sculptMesh" %splitNode,f=True)
				self.getSplitShapeOuts(splitMesh,-(i+1)*zWeight)
		
	def test(self):

		print "shape cmd test"


if __name__ == "__main__":
	p = ShapeCmd()
	p.getBlendShapeInfo()