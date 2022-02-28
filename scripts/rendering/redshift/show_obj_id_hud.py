#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
"""

import maya.cmds as cmds


def object_id(*args):
    try:
        selection = cmds.ls(sl=True)
        children = cmds.listRelatives(selection, shapes=True)
        ids = {}
        if len(children) == 1:
            return cmds.getAttr('%s.rsObjectId' % children[0])
        for node in children:
            ids[node] = cmds.getAttr('%s.rsObjectId' % node)

        return ', '.join([f'{x}: {y}' for x, y in ids.items()])
    except:
        return None


def main():
    """docstring for main"""
    cmds.headsUpDisplay('HUDObjectId', rem=True)
    cmds.headsUpDisplay(rp=(7, 0))
    cmds.headsUpDisplay('HUDObjectId', section=1, block=0, blockSize='medium', label='Object ID',
                        labelFontSize='large', dataFontSize='large', command=object_id, event='SelectionChanged',
                        nodeChanges='attributeChange')


if __name__ == '__main__':
    main()
