#!/usr/bin/env python
"""
search_and_replace_filename.py
Does a search and replace on selected file nodes.
"""
import maya.cmds as cmds


def main():

    sel_nodes = cmds.ls(sl=True)

    search_for = 'input'
    replace_with = 'output'

    for node in sel_nodes:
        if cmds.nodeType(node) == 'file':
            texture_path = cmds.getAttr(node + ".fileTextureName")
            new_texture_path = texture_path.replace(search_for, replace_with)
            cmds.setAttr(
                "{}.fileTextureName".format(node),
                new_texture_path,
                type='string')

            print "Path changed from " + texture_path + " to " + new_texture_path + " on node " + node


if __name__ == '__main__':
    main()