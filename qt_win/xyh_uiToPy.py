#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :xyh_uiToPy.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.8
##-----------------------------------------------------------


import sys,pprint
from pysideuic import compileUi

import maya.cmds as mc
import maya.mel as  mel
import maya.OpenMaya as om
import pymel.core as pm


def pysdieConvert():
	"""
	@convert ui file to the python file
	"""
	uiPath = mc.fileDialog2(ff="*ui",dialogStyle=1,fileMode=1)[0]
	pyPath = uiPath.replace(".ui","_ui.py")
	pyFile = open(pyPath,"w")
	compileUi(uiPath,pyFile,False,4,False)
	pyFile.close()


if __name__ == "__main__":

	pysdieConvert()