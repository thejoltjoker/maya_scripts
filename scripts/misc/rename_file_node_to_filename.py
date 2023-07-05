"""
rename_file_node_to_filename.py

Rename file nodes in maya to be the name of the input file.
"""
import os
import maya.cmds as cmds


def rename_selected_node_to_filename():
    sel_nodes = cmds.ls(sl=True)

    for node in sel_nodes:
        if cmds.nodeType(node) == 'file':
            texturePath = cmds.getAttr(node + ".fileTextureName")
            filenameExt = os.path.basename(texturePath)
            filename = os.path.splitext(filenameExt)[0] + '_FILE'
            cmds.rename(node, filename)


def main():
    """docstring for main"""
    rename_selected_node_to_filename()


if __name__ == '__main__':
    main()
