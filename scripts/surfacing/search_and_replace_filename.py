#!/usr/bin/env python
"""
search_and_replace_filename.py
Does a search and replace on selected file nodes.
"""
import maya.cmds as cmds


def search_replace_filename(input_string, output_string):
    print(input_string, output_string)


sel_nodes = cmds.ls(sl=True, type='file')

search_for = input_string
replace_with = output_string

for node in sel_nodes:
    texture_path = cmds.getAttr(node + ".fileTextureName")
    if search_for in texture_path:
        new_texture_path = texture_path.replace(search_for, replace_with)
        cmds.setAttr("{}.fileTextureName".format(node),
                     new_texture_path,
                     type='string')

        print("Path changed from " + texture_path + " to " + new_texture_path + " on node " + node)

if __name__ == '__main__':
    input_string = cmds.promptDialog(
        title='Search and Replace',
        message='Search for:',
        button=['OK...', 'Cancel'],
        defaultButton='OK...',
        cancelButton='Cancel',
        dismissString='Cancel')

    if input_string == 'OK...':
        input_string = cmds.promptDialog(query=True, text=True)
        if not input_string:
            cmds.warning('You must enter a search string')
            exit()

    output_string = cmds.promptDialog(
        title='Search and Replace',
        message='Replace with:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if output_string == 'OK':
        output_string = cmds.promptDialog(query=True, text=True)
    else:
        output_string = ''

    search_replace_filename(input_string, output_string)
