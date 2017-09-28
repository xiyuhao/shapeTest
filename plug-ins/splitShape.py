#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :splitShape.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.OpenMayaMPx as omPx
import maya.OpenMayaAnim as omAnim
import maya.OpenMaya as om
import pymel.core as pm
import maya.cmds as mc 


API_VERSION = om.MGlobal.apiVersion()


class SplitShapeDeformer(omPx.MPxDeformerNode):

	kPluginNodeName = "splitShapeDeformer"
	kPluginNodeId = om.MTypeId(0xabc004)
	aInputs = om.MObject()
	aMesh = om.MObject()
	aSkin = om.MObject()

	def __init__(self):

		super(SplitShapeDeformer,self).__init__()

		self._movePoints = {}
		self._weights = {}
		self._inputs = []

		self._inputsDirty = True
		self._meshDirty = True
		self._skinDirty = True

	def deform(self,data,itGeo,localToWorldMatrix,geomIndex):

		env = data.inputValue(self.envelope).asFloat()
		if not env:
			return 
		print "env ok"
		if self._meshDirty:
			meshObj = data.inputValue(SplitShapeDeformer.aMesh).data()
			if meshObj.isNull():
				return 
			else:
				fnMeshDag = om.MFnDagNode(meshObj)
				meshDag = om.MDagPath()
				fnMeshDag.getPath(meshDag)
				self._movePoints = {}
				self.getInputMeshPoints(meshDag)
				self._meshDirty = False
		if self._skinDirty:
			mfndg = om.MFnDependencyNode(self.thisMObject())
			skinMessagePlug = mfndg.findPlug(SplitShapeDeformer.aSkin)
			plugArray = om.MPlugArray()
			skinMessagePlug.connectedTo(plugArray,True,False)
			if plugArray.length() > 0:
				skinPlug = plugArray[0]
				self._weights = {}
				self.getSkinWeights(skinPlug)
				self._skinDirty = False
			else:
				return 
		if self._inputsDirty:
			self._inputs = []
			hInputs = data.inputArrayValue(SplitShapeDeformer.aInputs)
			num = hInputs.elementCount()
			if num:
				for i in range(num):
					value = hInputs.inputValue().asFloat()
					self._inputs.append(value)
					if i != (num-1):
						hInputs.next()
				self._inputsDirty = False
			else:
				return 
		if len(self._weights) != len(self._inputs):
			return
		while not itGeo.isDone():
			index = itGeo.index()
			w = 0
			for i,value in enumerate(self._inputs):
				w += value * self._weights[i][index]
			w = w * env
			#print env
			offsetPoint = self._movePoints[index]
			offsetVect = om.MVector(offsetPoint)
			if index == 0:
				print offsetVect.x,offsetVect.y,offsetVect.z
			currentPoint = itGeo.position()
			currentPoint += offsetVect
			itGeo.setPosition(currentPoint)
			itGeo.next()

	def setDependentsDirty(self,plug,plugArray):
		"""
		@set dependents dirty
		"""
		if plug == self.aInputs:
			self._inputsDirty = True
		elif plug == self.aMesh:
			self._meshDirty = True
		elif plug == self.aSkin:
			self._skinDirty=True

	def getInputMeshPoints(self,mesh):
		"""
		@get input mesh points
		"""
		itGeo = om.MItGeometry(mesh)
		i = 0
		if not itGeo.isDone():
			point = itGeo.position(om.MSpace.kWorld)
			print point.x,point.y,point.z
			self._movePoints[i] = point
			i += 1
			itGeo.next()

	def getSkinWeights(self,plug):
		"""
		@get skin weights
		"""
		skin = plug.node()
		if skin.hasFn(om.MFn.kSkinClusterFilter):
			fnSkin = omAnim.MFnSkinCluster(skin)
			skinObjPath = om.MDagPath()
			index = 0
			fnSkin.indexForOutputConnection(index)
			fnSkin.getPathAtIndex(index,skinObjPath)
			infs = om.MDagPathArray()
			numInfs = fnSkin.influenceObjects(infs)
			for i in range(numInfs):
				itGeo = om.MItGeometry(skinObjPath)
				self._weights[i] = []
				while not itGeo.isDone():
					wtArray = om.MDoubleArray()
					compObj = itGeo.component()
					fnSkin.getWeights(skinObjPath,compObj,i,wtArray)
					self._weights[i].append(wtArray[0])
					itGeo.next()

def nodeCreator():
	return omPx.asMPxPtr(SplitShapeDeformer())

def nodeInitialize():
	nAttr = om.MFnNumericAttribute()
	tAttr = om.MFnTypedAttribute()
	mAttr = om.MFnMessageAttribute()

	if API_VERSION < 201600:
		outputGeom = omPx.cvar.MPxDeformerNode_outputGeom
	else:
		outputGeom = omPx.cvar.MPxGeometryFilter_outputGeom

	SplitShapeDeformer.aInputs = nAttr.create("inputs","inputs",om.MFnNumericData.kFloat,0.0)
	nAttr.setMin(0.0)
	nAttr.setMax(1.0)
	nAttr.setStorable(True)
	nAttr.setKeyable(True)
	nAttr.setArray(True)
	nAttr.setUsesArrayDataBuilder(True)

	SplitShapeDeformer.aMesh = tAttr.create("inputMesh","inputMesh",om.MFnData.kMesh)
	tAttr.setConnectable(True)

	SplitShapeDeformer.aSkin = mAttr.create("skinNode","skinNode")

	SplitShapeDeformer.addAttribute(SplitShapeDeformer.aInputs)
	SplitShapeDeformer.addAttribute(SplitShapeDeformer.aMesh)
	SplitShapeDeformer.addAttribute(SplitShapeDeformer.aSkin)

	SplitShapeDeformer.attributeAffects(SplitShapeDeformer.aInputs,outputGeom)
	SplitShapeDeformer.attributeAffects(SplitShapeDeformer.aMesh,outputGeom)
	SplitShapeDeformer.attributeAffects(SplitShapeDeformer.aSkin,outputGeom)

def initializePlugin(mobject):
	mplugin = omPx.MFnPlugin(mobject,"xiyuhao","1.0")
	mplugin.registerNode(SplitShapeDeformer.kPluginNodeName,SplitShapeDeformer.kPluginNodeId,
						nodeCreator,nodeInitialize,omPx.MPxNode.kDeformerNode)

def uninitializePlugin(mobject):
	mplugin = omPx.MFnPlugin(mobject,"xiyuhao","1.0")
	mplugin.deregisterNode(SplitShapeDeformer.kPluginNodeId)