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


class ShapeCmd(object):

	def __init__(self):

		pass

	def test(self):

		print "shape cmd test"


if __name__ == "__main__":
	p = ShapeCmd()
	p.test()