#!/usr/bin/env python3
"""dromedary.py
Description of dromedary.py.
"""
from maya import cmds, mel
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QSizePolicy
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance


def create_bounding_box(node):
    bbox = cmds.exactWorldBoundingBox(node)
    curve_data = {'name': f'{node}_ctrl',
                  'knot': range(0, 16),
                  'point': [(bbox[0], bbox[4], bbox[2]),
                            (bbox[3], bbox[4], bbox[2]),
                            (bbox[3], bbox[1], bbox[2]),
                            (bbox[3], bbox[4], bbox[2]),
                            (bbox[3], bbox[4], bbox[5]),
                            (bbox[3], bbox[1], bbox[5]),
                            (bbox[3], bbox[4], bbox[5]),
                            (bbox[0], bbox[4], bbox[5]),
                            (bbox[0], bbox[1], bbox[5]),
                            (bbox[0], bbox[4], bbox[5]),
                            (bbox[0], bbox[4], bbox[2]),
                            (bbox[0], bbox[1], bbox[2]),
                            (bbox[3], bbox[1], bbox[2]),
                            (bbox[3], bbox[1], bbox[5]),
                            (bbox[0], bbox[1], bbox[5]),
                            (bbox[0], bbox[1], bbox[2])],
                  'degree': 1.0
                  }

    bbox_curve = cmds.curve(**curve_data)
    cmds.xform(bbox_curve, centerPivots=True, preserve=True)
    return bbox_curve


def origin_locator():
    if cmds.ls('origin_loc'):
        origin = cmds.ls('origin_loc')[0]
    else:
        origin = cmds.spaceLocator(name='origin_loc', p=[0, 0, 0])
    return origin


def explode():
    # Get all selected meshes
    nodes = cmds.ls(selection=True)

    # Create a locator at origin to aim at later
    origin = origin_locator()
    trash = []
    geo = []
    ctrl = []
    # Create display layers for the meshes as well as controls
    geo_layer = 'geo_layer' if cmds.ls('geo_layer') else cmds.createDisplayLayer(name='geo_layer')
    ctrl_layer = 'ctrl_layer' if cmds.ls('ctrl_layer') else cmds.createDisplayLayer(name='ctrl_layer')

    for mesh in nodes:
        bbox_curve = create_bounding_box(mesh)

        bbox_curve_pos = cmds.xform(bbox_curve, q=True, sp=True, ws=True)

        # Create stand in locator to aim
        aim_locator = cmds.spaceLocator(p=[0, 0, 0])
        cmds.xform(aim_locator, translation=bbox_curve_pos)
        cmds.makeIdentity(aim_locator, t=True, r=True, s=True, apply=True)

        # Aim bbox towards origin
        aim = cmds.aimConstraint(origin, aim_locator,
                                 offset=[0, 0, 0],
                                 weight=1,
                                 aimVector=[0, 0, 1],
                                 upVector=[0, 1, 0],
                                 worldUpType='vector',
                                 worldUpVector=[0, 1, 0])
        cmds.delete(aim)

        # Copy pivot from aim locator to bbox
        cmds.select(bbox_curve)
        cmds.select(aim_locator, add=True)
        mel.eval('MatchPivots; performMatchPivots 0;')

        # Parent constrain bbox to mesh
        cmds.parentConstraint(bbox_curve, mesh, mo=True, weight=1)

        geo.append(mesh)
        ctrl.append(bbox_curve)
        trash.append(aim_locator)
        cmds.select(clear=True)
    # Add members to display layers

    cmds.editDisplayLayerMembers(geo_layer, *geo)
    cmds.editDisplayLayerMembers(ctrl_layer, *ctrl)
    cmds.group(name='control_grp', *ctrl)

    # Empty trash
    for i in trash:
        cmds.delete(i)


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.setParent(mayaMainWindow)

        # Set window properties
        self.setWindowTitle('Explode')
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint)
        self.setMinimumSize(250, 300)

        font = QtGui.QFont("Source Sans Pro")
        font.setStyleHint(QtGui.QFont.SansSerif)
        self.setFont(font)

        # Create button widgets
        self.button_origin = QtWidgets.QPushButton('Create origin locator')
        self.button_explode = QtWidgets.QPushButton('Explode')

        # Instructions
        instructions_layout = QtWidgets.QVBoxLayout()
        instructions_layout.addWidget(QtWidgets.QLabel('Instructions'))
        instructions_layout.addWidget(QtWidgets.QLabel('1. Create origin locator and place it in center of explode'))
        instructions_layout.addWidget(QtWidgets.QLabel('2. Select geo to explode'))
        instructions_layout.addWidget(QtWidgets.QLabel('3. Run explode action'))
        instructions_layout.addWidget(QtWidgets.QLabel('4. Animate new controls'))

        # Main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(instructions_layout)
        main_layout.addStretch()
        main_layout.addWidget(self.button_origin)
        main_layout.addWidget(self.button_explode)
        self.setLayout(main_layout)

        # Connect button signals to slots
        self.button_origin.clicked.connect(origin_locator)
        self.button_explode.clicked.connect(explode)


def main():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    ui = Window(mayaMainWindow)
    ui.show()
    return ui


if __name__ == '__main__':
    main()
