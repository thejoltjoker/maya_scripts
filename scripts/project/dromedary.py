#!/usr/bin/env python3
"""explode_parts.py
Description of explode_parts.py.
"""
import math
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
    """
    This function locates the position of the 'explode_origin_loc' object in the scene. If it already exists, it will
    return the object. Otherwise, it will create a new spaceLocator object at the origin and return it.

    Returns:
    str: The name of the 'explode_origin_loc' object in the scene, either the pre-existing object or the newly created
    spaceLocator object.
    """
    name = 'explode_origin_loc'
    if cmds.ls(name):
        # If the object already exists in the scene, return it
        origin = cmds.ls(name)[0]
    else:
        # If the object doesn't exist, create a new spaceLocator object at the origin
        origin = cmds.spaceLocator(name=name, p=[0, 0, 0])

    # Select the origin object and return its name
    cmds.select(origin)
    return origin


def create_controls(nodes, origin, diff: float):
    # Create a locator at origin to aim at later
    origin = origin
    diff = diff
    trash = []
    geo = []
    l_ctrl = []
    r_ctrl = []
    c_ctrl = []
    # Create display layers for the meshes as well as controls
    geo_layer = 'geo_layer' if cmds.ls('geo_layer') else cmds.createDisplayLayer(name='geo_layer')
    l_ctrl_layer = 'L_ctrl_layer' if cmds.ls('L_ctrl_layer') else cmds.createDisplayLayer(name='L_ctrl_layer')
    r_ctrl_layer = 'R_ctrl_layer' if cmds.ls('R_ctrl_layer') else cmds.createDisplayLayer(name='R_ctrl_layer')
    c_ctrl_layer = 'C_ctrl_layer' if cmds.ls('C_ctrl_layer') else cmds.createDisplayLayer(name='C_ctrl_layer')

    # Loop through all selected nodes
    for selected_node in nodes:
        # Create a bounding box around the selected node
        bbox = create_bounding_box(selected_node)
        bbox_pos = cmds.xform(bbox, q=True, sp=True, ws=True)

        # Get the X position of the selected node and the reference node
        # selected_node_pos = cmds.xform(bbox, query=True, translation=True, worldSpace=True)
        selected_node_pos = bbox_pos
        # origin_pos = cmds.xform(origin, query=True, translation=True, worldSpace=True)
        origin_pos = cmds.xform(origin, q=True, sp=True, ws=True)
        selected_node_x = selected_node_pos[0]
        origin_x = origin_pos[0]
        origin_y = origin_pos[1]
        origin_y = origin_pos[2]

        # Color the bbox red if it's right of the reference node, blue if it's left of the reference node, yellow if it's not on either side
        if selected_node_x < origin_x - diff:
            cmds.setAttr(bbox + ".overrideColor", 13)  # Red
            # Rotate pivot of bbox
            cmds.setAttr(f'{bbox}.sx', -1)
            r_ctrl.append(bbox)
        elif selected_node_x > origin_x + diff:
            cmds.setAttr(bbox + ".overrideColor", 6)  # Blue
            l_ctrl.append(bbox)
        else:
            cmds.setAttr(bbox + ".overrideColor", 17)  # Yellow
            c_ctrl.append(bbox)

        # Parent constrain bbox to mesh
        cmds.parentConstraint(bbox, selected_node, mo=True, weight=1)

        geo.append(selected_node)

        cmds.select(clear=True)

    # Add members to display layers
    cmds.editDisplayLayerMembers(geo_layer, *geo)
    cmds.editDisplayLayerMembers(l_ctrl_layer, *l_ctrl)
    cmds.editDisplayLayerMembers(r_ctrl_layer, *r_ctrl)
    cmds.editDisplayLayerMembers(c_ctrl_layer, *c_ctrl)

    change_display_layer_color(l_ctrl_layer, 6)
    change_display_layer_color(r_ctrl_layer, 13)
    change_display_layer_color(c_ctrl_layer, 17)

    ctrl = l_ctrl
    ctrl.extend(r_ctrl)
    ctrl.extend(c_ctrl)
    cmds.group(name='explode_ctrl_grp', *ctrl)

    # Empty trash
    for i in trash:
        cmds.delete(i)


def change_display_layer_color(layer, color_index):
    cmds.setAttr(f'{layer}.displayType', 0)
    cmds.setAttr(f'{layer}.color', color_index)
    cmds.setAttr(f'{layer}.overrideColorRGB', 0, 0, 0)
    cmds.setAttr(f'{layer}.overrideRGBColors', 0)
    return layer


AXIS = {'x+': 0,
        'x-': 0,
        'y+': 1,
        'y-': 1,
        'z+': 2,
        'z-': 2}


def move_away_from_origin(nodes, origin, axis, distance):
    axis_int = AXIS.get(axis)
    # Get the center of the scene
    center = cmds.xform(origin, query=True, worldSpace=True, sp=True)

    # Loop through the selected objects
    for obj in nodes:
        # Get the object's position
        pos = cmds.xform(obj, query=True, worldSpace=True, sp=True)

        # Calculate the distance from the center
        dist = math.sqrt((pos[axis_int] - center[axis_int]) ** 2)
        if axis.endswith('-'):
            dist = dist * -1
        # Move the object away from the center based on its distance
        translate = [0, 0, 0]

        if dist != 0:
            translate[axis_int] = pos[axis_int] + (pos[axis_int] - center[axis_int]) / dist * distance
            cmds.move(*translate, obj, relative=True)
    cmds.select(*nodes)
    return nodes


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

        # Instructions
        instructions_box = QtWidgets.QGroupBox('Instructions')
        instructions_layout = QtWidgets.QVBoxLayout()
        instructions_layout.addWidget(QtWidgets.QLabel('Instructions'))
        instructions_layout.addWidget(QtWidgets.QLabel('1. Create origin locator and place it in center of explode'))
        instructions_layout.addWidget(QtWidgets.QLabel('2. Select geo to explode'))
        instructions_layout.addWidget(QtWidgets.QLabel('3. Create controls'))
        instructions_layout.addWidget(QtWidgets.QLabel('4. Animate new controls'))
        instructions_box.setLayout(instructions_layout)

        # Create button widgets
        setup_box = QtWidgets.QGroupBox('Setup')
        setup_layout = QtWidgets.QFormLayout()
        self.button_origin = QtWidgets.QPushButton('Create locator')
        setup_layout.addRow('Origin locator', self.button_origin)
        self.line_ctrl_offset = QtWidgets.QLineEdit()
        self.line_ctrl_offset.setPlaceholderText('Units from origin that are considered centered')
        setup_layout.addRow('Controls center zone', self.line_ctrl_offset)
        self.button_controls = QtWidgets.QPushButton('Create controls')
        setup_layout.addRow('Controls', self.button_controls)
        # Connect button signals to slots
        self.button_origin.clicked.connect(origin_locator)
        self.button_controls.clicked.connect(self.create_controls)
        setup_layout.addWidget(self.button_origin)
        setup_layout.addWidget(self.button_controls)
        setup_box.setLayout(setup_layout)

        # Animation
        animation_box = QtWidgets.QGroupBox('Animation')
        animation_layout = QtWidgets.QFormLayout()
        animation_axis_layout = QtWidgets.QGridLayout()
        axises = ['x+', 'x-', 'y+', 'y-', 'z+', 'z-']
        count = 0
        row = 0
        col = 0
        for axis in axises:
            if count % 2 == 1:
                row += 1
            else:
                col += 1
                row = 0
            count += 1
            button = QtWidgets.QPushButton(axis)

            button.clicked.connect(self.move_objects)
            animation_axis_layout.addWidget(button, row, col)
        # self.line_spread = QtWidgets.QLineEdit()
        self.line_distance = QtWidgets.QLineEdit()
        # animation_layout.addRow('Spread', self.line_spread)
        animation_layout.addRow('Distance', self.line_distance)
        animation_layout.addRow('Axis', animation_axis_layout)
        animation_box.setLayout(animation_layout)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addWidget(instructions_box)
        main_layout.addWidget(setup_box)
        main_layout.addWidget(animation_box)
        self.setLayout(main_layout)

    def move_objects(self):
        axis = self.sender().text()
        distance = float(self.line_distance.text()) if self.line_distance.text() else 0.0
        nodes = cmds.ls(selection=True)
        move_away_from_origin(nodes, origin_locator(), axis, distance)

    def create_controls(self):
        diff = float(self.line_ctrl_offset.text()) if self.line_ctrl_offset.text() else 0.0
        # Get all selected meshes
        nodes = cmds.ls(selection=True)
        create_controls(nodes, origin_locator(), diff)


def main():
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    ui = Window(mayaMainWindow)
    ui.show()
    return ui


if __name__ == '__main__':
    main()
