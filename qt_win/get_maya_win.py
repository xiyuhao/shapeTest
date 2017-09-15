#!/usr/bin/python
# -*- coding: utf-8 -*-

##----------------------------------------------------------
##file :get_maya_win.py
##author:xiyuhao
##email:695888835@qq.com
##----------------------------------------------------------
##date:2017.9.15
##-----------------------------------------------------------


import sys
import os

import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
import shiboken as PyQtSip

import maya.OpenMayaUI as omui


def getMayaWin():
	"""
	@get the maya window
	"""
	ptr = omui.MQtUtil.mainWindow()
	inptr = PyQtSip.wrapInstance(long(ptr),QtGui.QWidget)
	return inptr