import sys
import os
import re
#from PySide2 import QtCore, QtWidgets
from PySide2 import QtWidgets
import maya.cmds as cmd
import maya.mel as mm
import pymel.core as pm
import mtoa.aovs as aovs
globIsoFlag = []

WINDOW_NAME = 'Tool'


def maya_main_window():
    import maya.OpenMayaUI as apiUI
    from shiboken2 import wrapInstance
    main_win_ptr = apiUI.MQtUtil.mainWindow()
    return wrapInstance(long(main_win_ptr), QtWidgets.QDialog)


class Dialog(QtWidgets.QDialog):

    def __init__(self, parent=None, show=True):
        super(Dialog, self).__init__(parent=parent)
        self.mainLayout = QtWidgets.QGridLayout(self)

        self.CopyTransformBox()

        self.mainLayout.addWidget(self.CopyTransformGBox, 0, 0, 1, 2)

        self.setLayout(self.mainLayout)

        if show:
            self.show()

    # Copy transform
    def CopyTransformBox(self):

        self.CopyTransformGBox = QtWidgets.QGroupBox("COPY  TRANSFORM")
        self.allTr = QtWidgets.QPushButton('ALL')
        self.Tr_translate = QtWidgets.QPushButton('Translate')
        self.Tr_rotate = QtWidgets.QPushButton('Rotate')

        CopyTransformLayout = QtWidgets.QGridLayout()
        CopyTransformLayout.addWidget(self.allTr, 2, 0, 1, 1)
        CopyTransformLayout.addWidget(self.Tr_translate, 2, 1, 1, 1)
        CopyTransformLayout.addWidget(self.Tr_rotate, 2, 2, 1, 1)
        self.CopyTransformGBox.setLayout(CopyTransformLayout)


def maya_ui():
    dialog = Dialog(parent=maya_main_window())


if __name__ == '__main__':
maya_ui()
