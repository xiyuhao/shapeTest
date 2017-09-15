#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :shape_win.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om
import pymel.core as pm

from get_maya_win import *

import shape_cmd
reload(shape_cmd)
import shape_win_ui
reload(shape_win_ui)

from shape_cmd import ShapeCmd
from shape_win_ui import Ui_shapeToolWin


class ShapeWin(Ui_shapeToolWin):

	def setupUi(self,shapeToolWin):

		Ui_shapeToolWin.setupUi(self,shapeToolWin)

		self.blendShapeTargetLinkPushButton.clicked.connect(lambda:self.test("link"))
		self.blendShapeTargetNoPushButton.clicked.connect(lambda:self.test("no"))
		self.blendShapeImportPushButton.clicked.connect(lambda:self.test("import"))
		self.blendShapeExportPushButton.clicked.connect(lambda:self.test("export"))

		self.shapeCmd = ShapeCmd()

	def test(self,str):

		self.shapeCmd.test()
		print "test the shape tool push %s" %str 


if __name__ == "__main__":

	if mc.window("shapeToolWin",exists=True):
		mc.deleteUI("shapeToolWin")
	mayaWindow = getMayaWin()
	print mayaWindow
	ui = ShapeWin()
	qtWindow = QtGui.QMainWindow(mayaWindow)
	ui.setupUi(qtWindow)
	qtWindow.show()