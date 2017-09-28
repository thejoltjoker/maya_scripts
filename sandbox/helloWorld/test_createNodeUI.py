# Copyright 2015 Autodesk, Inc. All rights reserved.
#
# Use of this software is subject to the terms of the Autodesk
# license agreement provided at the time of installation or download,
# or which otherwise accompanies this software in either electronic
# or hard copy form.

from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui

try:
  from PySide2.QtCore import *
  from PySide2.QtGui import *
  from PySide2.QtWidgets import *
  from PySide2.QtUiTools import *
  from shiboken2 import wrapInstance
except ImportError:
  from PySide.QtCore import *
  from PySide.QtGui import *
  from PySide.QtUiTools import *
  from shiboken import wrapInstance


import os.path

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(long(mayaMainWindowPtr), QMainWindow)

class CreateNodeUI(QWidget):
    def __init__(self, *args, **kwargs):
        super(CreateNodeUI,self).__init__(*args, **kwargs)
        self.setParent(mayaMainWindow)
        self.setWindowFlags( Qt.Window )
        self.initUI()

    def initUI(self):
        loader = QUiLoader()
        currentDir = os.path.dirname(__file__)
        file = QFile(currentDir+"/test_createNode.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, parentWidget=self)
        file.close()

        self.ui.btnOk.clicked.connect( self.doOK )
        self.ui.btnCancel.clicked.connect( self.doCancel )


    def doOK(self):
        self.close()

    def doCancel(self):
        self.close()


def main():
    ui = CreateNodeUI()
    ui.show()
    return ui


if __name__ == '__main__':
    main()
