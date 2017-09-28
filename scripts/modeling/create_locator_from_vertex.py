#!/usr/bin/env python
"""
create_locator_from_vertex.py
Description of create_locator_from_vertex.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    vertices = cmds.ls(sl=True)
    if any('.vtx' in v for v in vertices):
        loc_size = 10

        for vertex in vertices:
            point_pos = cmds.pointPosition(vertex)
            loc = cmds.spaceLocator(p=tuple(point_pos))
            shapes = cmds.listRelatives(loc)
            for shape in shapes:
                cmds.setAttr("{}.localScaleX".format(shape), loc_size)
                cmds.setAttr("{}.localScaleY".format(shape), loc_size)
                cmds.setAttr("{}.localScaleZ".format(shape), loc_size)
    else:
        cmds.warning("No vertices selected!")


if __name__ == '__main__':
    main()
