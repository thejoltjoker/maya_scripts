#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""
import maya.cmds as cmds
import maya.mel as mel
import logging
import pymel.core as pm

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)


def get_selected_vertices():
    selection = cmds.ls(sl=True, fl=True)
    verts = [x for x in selection if '.vtx' in x]
    if not verts:
        cmds.warning("No vertices selected!")

    return verts


def locator_name():
    num = 1
    # Create new name for locator
    new_locator_name = 'Null{:03d}_aeNull'.format(num)
    while new_locator_name in cmds.ls():
        new_locator_name = 'Null{:03d}_aeNull'.format(num)
        num += 1
    return new_locator_name


def create_locator_on_vertex(vertex, constrain=False, size=1):
    new_locator_name = locator_name()

    # Get position of vertex
    point_pos = cmds.pointPosition(vertex)

    # Create locator
    locator = cmds.spaceLocator(p=tuple(point_pos), n=new_locator_name)

    # Scale the locator
    # shapes = cmds.listRelatives(locator, s=True)
    # for shape in shapes:
    #     cmds.setAttr("{}.localScaleX".format(shape), size)
    #     cmds.setAttr("{}.localScaleY".format(shape), size)
    #     cmds.setAttr("{}.localScaleZ".format(shape), size)
    # cmds.makeIdentity(locator, apply=True, scale=True)

    # Constrain to vertex
    if constrain:
        constrain_to_vertex(vertex, locator)

    return locator


def create_locators_from_vertices(vertices, constrain=False, size=1):
    """Create locators from vertices"""
    locators = []
    for num, vertex in enumerate(vertices):
        locator = create_locator_on_vertex(vertex, constrain=constrain, size=size)
        locators.append(locator)
    return locators


def constrain_to_vertex(vertex, node):
    cmds.select(vertex)
    cmds.select(node, add=True)
    # cmds.select(vertex, node, r=True)
    # mel.eval('doCreatePointOnPolyConstraintArgList 2 {   "0" ,"0" ,"0" ,"1" ,"" ,"1" ,"0" ,"0" ,"0" ,"0" };')
    # cmds.pointOnPolyConstraint(vertex, node)
    # mel.eval('pointOnPolyConstraint -offset 0 0 0  -weight 1;')
    pm.runtime.PointOnPolyConstraint()

def main():
    """docstring for main"""
    vertices = get_selected_vertices()
    logger.info(vertices)
    locators = create_locators_from_vertices(vertices, constrain=True, size=2)
    logger.info(locators)


if __name__ == '__main__':
    main()
