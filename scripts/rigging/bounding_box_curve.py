#!/usr/bin/env python3
"""bounding_box_curve.py
Create a bounding box curve around the selected object
Source: https://www.reddit.com/r/Maya/comments/k3v3dk/bounding_box_to_nurbs_control/
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    selection = cmds.ls(selection=True)
    for node in selection:
        try:
            bbox = cmds.exactWorldBoundingBox(node)
            curve_data = {"knots": range(0, 16),
                          "points": [(bbox[0], bbox[4], bbox[2]),
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
                                     (bbox[0], bbox[1], bbox[2])]
                          }

            bbox_curve = cmds.curve(name=f'{node}_bbox_ctrl',
                                    degree=1.0,
                                    point=curve_data['points'],
                                    knot=curve_data['knots'])
            cmds.select(clear=True)
        except TypeError:
            pass

    cmds.select(selection, replace=True)


if __name__ == '__main__':
    main()
