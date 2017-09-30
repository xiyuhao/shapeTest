#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :x_skin.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm


class XSkin(object):
	"""the skinCluster class"""
	def __init__(self):
		"""
		@the skinCluster class initialization
		"""
		pass

	def getSkinInfs(self,skinNode):
		"""
		@get the skin node infs
		"""
		if mc.objectType(skinNode) != "skinCluster":
			return 
		infs = mc.skinCluster(skinNode,q=True,influence=True)
		return infs

	def getSkinWeight(self,skinNode):
		"""
		@get skin node weights
		"""
		weights = {}
		if mc.objectType(skinNode) != "skinCluster":
			return
		pmSkin = pm.PyNode(skinNode)
		pmInfs = pmSkin.getInfluence()
		pmGeo = pmSkin.getGeometry()[0]
		for i,inf in enumerate(pmInfs):
			weight = []
			wtItr = pmSkin.getWeights(pmGeo,i)
			for wt in wtItr:
				weight.append(wt)
			weights[i] = weight
		return weights


if __name__ == "__main__":

	p = XSkin()
	p.getSkinWeight("skinCluster1")