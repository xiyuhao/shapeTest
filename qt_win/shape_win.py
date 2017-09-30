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

from qt_win.get_maya_win import *

from qt_win import shape_cmd
reload(shape_cmd)
from qt_win import shape_win_ui
reload(shape_win_ui)

from qt_win.shape_cmd import ShapeCmd
from qt_win.shape_win_ui import Ui_shapeToolWin


class ShapeWin(Ui_shapeToolWin):

	def setupUi(self,shapeToolWin):

		Ui_shapeToolWin.setupUi(self,shapeToolWin)

		self.blendShapeTargetSelectPushButton.clicked.connect(
								lambda:self.blendShapeTargetSelectButtonCmd())
		self.blendShapeTargetLinkPushButton.clicked.connect(
								lambda:self.blendShapeTargetLinkButtonCmd())
		self.blendShapeTargetNoPushButton.clicked.connect(
								lambda:self.blendShapeTargetNoButtonCmd())
		self.blendShapeImportPushButton.clicked.connect(lambda:self.test("import"))
		self.blendShapeExportPushButton.clicked.connect(lambda:self.test("export"))
		self.splitShapeCreatePushButton.clicked.connect(
								lambda:self.splitShapeCreatePushButtonCmd())
		self.splitShapeSplitPushButton.clicked.connect(
								lambda:self.splitShapeSplitPushButtonCmd())

		self.shapeCmd = ShapeCmd()

		if not mc.pluginInfo("splitShape.mll",q=True,loaded=True):
			try:
				mc.loadPlugin("splitShape.mll",quiet=True)
			except:
				print "load splitShape is failed"

	def setTreeWidgetText(self,widget,infos):
		"""
		@set the given list widget text
		"""
		widget.clear()
		if not infos:
			return
		for i,node in enumerate(infos):
			nodeItem = QtGui.QTreeWidgetItem(widget)
			nodeItem.setText(0,"Node: %s" %node)
			widget.insertTopLevelItem(i,nodeItem)
			for tran in infos[node]:
				tranItem = QtGui.QTreeWidgetItem(nodeItem)
				tranItem.setText(0,"Geometry: %s" %tran)
				for name in infos[node][tran]:
					nameItem = QtGui.QTreeWidgetItem(tranItem)
					nameItem.setText(0,"WeightName: %s" %name)
					for weight in infos[node][tran][name]:
						weightItem = QtGui.QTreeWidgetItem(nameItem)
						weightItem.setText(0,"Weight: %s" %weight)

	def getTreeWidgetSelectedItem(self,widget):
		"""
		@get the selected item for the given lsitWidget
		"""
		texts = []
		items = widget.selectedItems()
		for item in items:
			text = item.text(0).split()[-1]
			parentItem = item.parent()
			while item.parent():
				parentText = item.parent().text(0).split()[-1]
				text = "%s %s" %(parentText,text)
				item = item.parent()
			texts.append(text)
		return texts

	def blendShapeTargetSelectButtonCmd(self):
		"""
		@the blendShape target select pushButton command
		"""
		blendShapeInfo = self.shapeCmd.getBlendShapeInfo()
		self.setTreeWidgetText(self.blendShapeTargetNameTreeWidget,blendShapeInfo)

	def blendShapeTargetLinkButtonCmd(self):
		"""
		@the blendShape target link pushButton command
		"""
		texts = self.getTreeWidgetSelectedItem(self.blendShapeTargetNameTreeWidget)
		self.shapeCmd.linkOrNoBlendShapeTarget(texts)

	def blendShapeTargetNoButtonCmd(self):
		"""
		@the blendShape target no link pushButton command
		"""
		texts = self.getTreeWidgetSelectedItem(self.blendShapeTargetNameTreeWidget)
		self.shapeCmd.linkOrNoBlendShapeTarget(texts,False)

	def splitShapeCreatePushButtonCmd(self):
		"""
		@the split shape create button command
		"""
		sels = mc.ls(sl=True,type="transform")
		if sels and len(sels) >=4:
			self.shapeCmd.createSplitShapeNode(sels[0],sels[1],sels[2],sels[3])
		else:
			print "please select the sculptObj,origObj,skinObj,outObj"

	def splitShapeSplitPushButtonCmd(self):
		"""
		@the split shape split button command
		"""
		sels = mc.ls(sl=True,type="transform")
		if not sels:
			print "please select splitShapeNode object"
		else:
			self.shapeCmd.batchGetSplitShapeOuts(sels)

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