#!/usr/bin/env python3
"""group.py
Group selected nodes and name the group appropriately
"""
from maya import cmds


def group(nodes, name=None):
    """Group nodes together and name the group

    Args:
        nodes (list): nodes to group together
        name (str): name of the new group. If none it will be named after the first node
    """
    name = name if name else nodes[0]

    return cmds.group(nodes, name=f'{name}_grp')


def main():
    """docstring for main"""
    nodes = cmds.ls(sl=True)
    ph = nodes[0]
    dialog_title = 'Group'
    dialog_message = 'Group name:'
    default_button = 'OK'
    cancel_button = 'Cancel'
    dialog = cmds.promptDialog(
        title=dialog_title,
        message=dialog_message,
        text=ph,
        button=[default_button, cancel_button],
        defaultButton=default_button,
        cancelButton=cancel_button,
        dismissString=cancel_button)

    if dialog == default_button:
        output = cmds.promptDialog(query=True, text=True)
        if output:
            # Do stuff here
            group(nodes, output)
        else:
            # If input is blank
            cmds.warning(dialog_title + ": The input can't be blank")
    else:
        # If dialog is cancelled
        print('User cancelled ' + dialog_title)


if __name__ == '__main__':
    main()
