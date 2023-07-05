#!/usr/bin/env python3
"""merge_curve_shapes.py
Select curve shapes you want to merge
"""
from maya import cmds


def get_control_points(shape):
    """

    Args:
        shape:

    Returns:
        list:
    """
    control_points = []
    control_point_count = cmds.getAttr(f'{shape}.controlPoints', size=True)
    for i in range(control_point_count):
        x = cmds.getAttr(f'{shape}.controlPoints[{i}].xValue')
        y = cmds.getAttr(f'{shape}.controlPoints[{i}].yValue')
        z = cmds.getAttr(f'{shape}.controlPoints[{i}].zValue')
        point = (x,y,z)
        control_points.append(point)
    # return cmds.listAttr(f'{shape}.controlPoints', multi=True)

    return control_points

def main():
    """Select curve shapes you want to merge"""
    points = []
    for shape in cmds.ls(sl=True, shapes=True):
        print(shape)
        p = get_control_points(shape)
        points.extend(p)
    cmds.curve(point=points)


if __name__ == '__main__':
    main()
