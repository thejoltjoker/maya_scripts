#!/usr/bin/env python3
"""walrus.py
Description of walrus.py.
"""
import string

from maya import cmds, mel
from OBB.api import OBB


def select_every_nth(nodes, distance=7, offset=0):
    light_set = []
    global_inc = 1
    inc = 1 + offset
    fixtures = []
    fixture = []
    stand = None
    for node in nodes:
        if inc == distance:
            fix = cmds.polyUnite(fixture, name=f'fixture{global_inc}', constructionHistory=False)
            obbBoundBoxPnts = OBB.from_points(fix)
            obbCube = cmds.polyCube(constructionHistory=False, name=f"bbox{global_inc}")[0]
            cmds.setAttr(f'{obbCube}.visibility', 0)
            cmds.xform(obbCube, matrix=obbBoundBoxPnts.matrix)
            # print(obbBoundBoxPnts.volume)
            light = cmds.shadingNode("RedshiftPhysicalLight", asLight=1, name=f'lightShape{global_inc}')
            cmds.setAttr(f'lightShape{global_inc}.areaShape', 1)
            """connectAttr -f locator1.lightsExposure lightShape90.exposure;"""
            cmds.connectAttr('lights_ctrl.lightsExposure', f'lightShape{global_inc}.exposure', f=True)
            light = cmds.rename(light, f'light{global_inc}')
            const = cmds.pointConstraint(obbCube, light, w=1, mo=False)
            cmds.delete(const, cn=True)
            const = cmds.orientConstraint(obbCube, light, w=1, mo=False, offset=(-90, 0, 0))
            cmds.delete(const, cn=True)
            cmds.scale(10, 10, 10, light)
            lamp = cmds.group(fix, stand, obbCube, light, name=f'lamp{global_inc}')
            light_set.append(light)

            # reset
            inc = 1
            fixture = []
            stand = None
            global_inc += 1
        elif inc == 1:
            stand = node
            inc += 1
        else:
            fixture.append(node)
            inc += 1
    cmds.select(light_set)
    return fixtures


def main():
    """docstring for main"""

    nodes = cmds.ls(sl=True)
    select_every_nth(nodes)
    # for node in nodes:
    #     obbBoundBoxPnts = OBB.from_points(node)
    #     obbCube = cmds.polyCube(constructionHistory=False, name="pointMethod_GEO")[0]
    #     cmds.xform(obbCube, matrix=obbBoundBoxPnts.matrix)
    #     print(obbBoundBoxPnts.volume)


if __name__ == '__main__':
    main()
