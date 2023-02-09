#!/usr/bin/env python3
"""center_pivot_bottom.py
Center the pivot of an object in x and z axis, y = 0.
"""
from maya import cmds


def main():
    """docstring for main"""
    sel = cmds.ls(sl=True)
    for obj in sel:
        center = cmds.objectCenter(obj, gl=True)
        center[1] = 0
        print('Setting pivot to {}'.format(center))
        cmds.move(center[0], center[1], center[2], obj + '.scalePivot', obj + '.rotatePivot', absolute=True)

        # cmds.xform(piv=center)


if __name__ == '__main__':
    main()
