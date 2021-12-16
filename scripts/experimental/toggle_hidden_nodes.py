#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
toggle_hidden_nodes.py
Description of toggle_hidden_nodes.py.
"""
import maya.cmds as cmds


def main(nodes):
    """docstring for main"""
    for node in nodes:
        if cmds.getAttr('{}.visibility'.format(node)):
            cmds.hide(node)
        else:
            cmds.showHidden(node)


if __name__ == '__main__':
    main(['KBL001_010_anim:MASH_L_DEST_ReproMesh',
          'KBL001_010_anim:MASH_R_DEST_ReproMesh',
          'KBL001_010_anim:MASH_FLOAT_DEST_ReproMesh'])
