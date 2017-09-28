#!/usr/bin/env python
"""
remove_foster_parents.py
Description of remove_foster_parents.py.
"""


def main():
    """docstring for main"""
    all_nodes = cmds.ls()

    for node in all_nodes:
        if cmds.nodeType(node) == 'fosterParent':
            cmds.delete(node)
            print("{} was deleted.".format(node))


if __name__ == '__main__':
    main()
