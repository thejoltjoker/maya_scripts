"""add_attribute.py
Add an attribute to selected nodes if it doesn't exist
"""
import os

from maya import cmds

FILE = os.path.join(os.path.expanduser('~'), '.recent_maya_attributes')


def add_attribute(node, attr_name, attr_type='float', value=None):
    if not cmds.attributeQuery(attr_name, node=node, ex=True):
        cmds.addAttr(node, ln=attr_name, at=attr_type, k=True)
        if value:
            cmds.setAttr(node + '.' + attr_name, value)


def save_recent_to_file(attr_name):
    path = FILE
    with open(path, 'w') as file:
        file.write(attr_name)


def get_recent_from_file(attr_name):
    path = FILE
    with open(path, 'r') as file:
        return file.read().strip()


def path_dialog(placeholder=None):
    text = placeholder if placeholder else os.path.dirname(cmds.file(q=True, exn=True))
    dialog_title = 'Images Path'
    dialog_message = 'Images path:'
    default_button = 'OK'
    cancel_button = 'Cancel'
    dialog = cmds.promptDialog(
        title=dialog_title,
        message=dialog_message,
        text=text,
        button=[default_button, cancel_button],
        defaultButton=default_button,
        cancelButton=cancel_button,
        dismissString=cancel_button)

    if dialog == default_button:
        output = cmds.promptDialog(query=True, text=True)
        if output:
            # Do stuff here
            set_images_path(text)
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")
    else:
        # If dialog is cancelled
        print('User cancelled ' + dialog_title)

def main():
    """docstring for main"""

    name_dialog = cmds.promptDialog(
        title='Add attribute',
        message='Enter attribute name:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if name_dialog == 'OK':
        name = cmds.promptDialog(query=True, text=True)
        if name:
            nodes = cmds.ls(sl=True)
            for node in nodes:
                add_attribute(node, name)
        else:
            cmds.warning("The attribute name can't be blank")
    else:
        print('User cancelled action')


if __name__ == '__main__':
    main()
