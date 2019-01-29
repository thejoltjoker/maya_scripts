"""
rename_shading_node_to_mtl_name.py
"""
import os
import re
import maya.cmds as cmds


def format_name(s):
    return re.sub(r'[\W_]+', '', s)


def main():
    sel_nodes = cmds.ls(sl=True, type='shadingEngine')
    materials = cmds.ls(mat=True)

    for node in sel_nodes:
        print node
        inputs = cmds.listConnections(node, s=True, d=False)
        for i in inputs:
            if i in materials:
                new_name = '{}_SG'.format(format_name(i))
                try:
                    cmds.rename(node, new_name)
                except Exception as e:
                    pass


if __name__ == "__main__":
    main()
