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

	def getBlendShapeWeightAttrFromText(self,texts):
		"""
		@get blendShape weight attrbiute from given text
		"""
		attrs = []
		if not texts:
			return
		if not isinstance(texts,list):
			texts = [texts]
		for text in texts:
			names = text.split()
			num = len(names)
			if num == 1:
				rAttrs = self.findBlendShapeAttrFromNodeName(names[0])
				attrs.extend(rAttrs)
			elif num == 2:
				rAttrs = self.findBlendShapeAttrFromGeoName(names[0],names[1])
				attrs.extend(rAttrs)
			elif num == 3:
				rAttrs = self.findBlendShapeAttrFromWeightName(names[0],names[1],names[2])
				attrs.extend(rAttrs)
			elif num == 4:
				rAttrs = self.findBlendShapeAttrFromWeightValue(names[0],names[1],names[2],names[3])
				attrs.extend(rAttrs)
			else:
				continue
		nAttrs = list(set(attrs))
		return nAttrs

	def findBlendShapeAttrFromNodeName(self,node):
		"""
		@find the blendShape attribute from blendShape node name
		"""
		attrs = []
		numGeos = mc.getAttr("%s.inputTarget" %node,multiIndices=True)
		for numGeo in numGeos:
			numNames = mc.getAttr("%s.inputTarget[%s].inputTargetGroup"
								 %(node,numGeo),multiIndices=True)
			for numName in numNames:
				numWeights = mc.getAttr(
						"%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem"
						%(node,numGeo,numName),multiIndices=True)
				for numWeight in numWeights:
					attr = "%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem[%s]" \
							%(node,numGeo,numName,numWeight)
					attrs.append(attr)
		return attrs

	def findBlendShapeAttrFromGeoName(self,node,geo):
		"""
		@find the blendShape attribute from blendShape geometry name
		"""
		attrs = []
		geoName = self.getBlendShapeGeometry(node)
		geoNum = mc.getAttr("%s.inputTarget" %node,multiIndices=True)
		geoIdx = geoName.index(geo)
		numGeo = geoNum[geoIdx]
		numNames = mc.getAttr("%s.inputTarget[%s].inputTargetGroup"
							 %(node,numGeo),multiIndices=True)
		for numName in numNames:
			numWeights = mc.getAttr(
					"%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem"
					%(node,numGeo,numName),multiIndices=True)
			for numWeight in numWeights:
				attr = "%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem[%s]" \
						%(node,numGeo,numName,numWeight)
				print attr
				attrs.append(attr)
		return attrs

	def findBlendShapeAttrFromWeightName(self,node,geo,name):
		"""
		@find blendShape attrbitue from weight name
		"""
		attrs = []
		geoName = self.getBlendShapeGeometry(node)
		geoNum = mc.getAttr("%s.inputTarget" %node,multiIndices=True)
		geoIdx = geoName.index(geo)
		numGeo = geoNum[geoIdx]
		weightName = self.getBlendShapeWeightName(node)
		nameNum = mc.getAttr("%s.inputTarget[%s].inputTargetGroup"
							 %(node,numGeo),multiIndices=True)
		nameIdx = weightName.index(name)
		numName = nameNum[nameIdx]
		numWeights = mc.getAttr(
				"%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem"
				%(node,numGeo,numName),multiIndices=True)
		for numWeight in numWeights:
			attr = "%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem[%s]" \
					%(node,numGeo,numName,numWeight)
			print attr
			attrs.append(attr)
		return attrs

	def findBlendShapeAttrFromWeightValue(self,node,geo,name,weight):
		"""
		@find blendShape attribute from weight value
		"""
		attrs = []
		geoName = self.getBlendShapeGeometry(node)
		geoNum = mc.getAttr("%s.inputTarget" %node,multiIndices=True)
		geoIdx = geoName.index(geo)
		numGeo = geoNum[geoIdx]
		weightName = self.getBlendShapeWeightName(node)
		nameNum = mc.getAttr("%s.inputTarget[%s].inputTargetGroup"
							 %(node,numGeo),multiIndices=True)
		nameIdx = weightName.index(name)
		numName = nameNum[nameIdx]
		numWeight = int(1000 * float(weight) + 5000)
		attr = "%s.inputTarget[%s].inputTargetGroup[%s].inputTargetItem[%s]" \
				%(node,numGeo,numName,numWeight)
		attrs.append(attr)
		return attrs

	def fromAttrGetNameInfo(self,attr):
		"""
		@from given attribute get name informations
		"""
		if not attr:
			return
		if not mc.objExists(attr):
			return
		node,geo,name,weight = attr.split(".")
		geoIdx = geo.split("[")[-1].split("]")[0]
		geoShapes = mc.blendShape(node,q=True,geometry=True)
		geoShape = geoShapes[int(geoIdx)]
		weightNameIdx = name.split("[")[-1].split("]")[0]
		weightNames = self.getBlendShapeWeightName(node)
		weightName = weightNames[int(weightNameIdx)]
		weightValue = weight.split("[")[-1].split("]")[0]
		return node,geoShape,weightName,weightValue

if __name__ == "__main__":

	p = XBlendShape()
	s = p.getBlendShapeWeightAttrFromText(["DD pSphere1 pSphere5 0.8","DD pSphere1 pSphere2 0.4"])