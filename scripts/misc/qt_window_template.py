#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
qt_window_template.py
Description of qt_window_template.py.
"""
from PyQt4 import QtCore, QtGui
import sip

import maya.cmds as cmds
import maya.OpenMayaUI as mui


class Window(QtGui.QDialog):

	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		
		# custom code here
		self.resize(800,600)


def getMainWindow():
	ptr = mui.MQtUtil.mainWindow()
	mainWin = sip.wrapinstance(long(ptr), QtCore.QObject)
	return mainWin


def show():
	win = Window(parent=getMainWindow())
	win.show()
	win.raise_()
	return win	

if __name__ == '__main__':
    show()