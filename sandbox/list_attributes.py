#!/usr/bin/env python
"""
list_attributes.py
<<<<<<< HEAD
Lists all attributes and their respective values, for selected object. Disregards attribute types: message, compound.
"""
import maya.cmds as cmds
=======
Description of list_attributes.py.
"""
>>>>>>> dd39bd6b508171453c9dc36e90b2d4418283fbb7


def main():
    """docstring for main"""
    all_nodes = cmds.ls(sl=True)
<<<<<<< HEAD
    for node in all_nodes:
        print("Attributes for {}".format(node))
        attribute_list = cmds.listAttr(node)
        for attr in attribute_list:
            if not '.' in attr:
                attribute_type = cmds.attributeQuery(attr, node=node, at=True)
                if attribute_type not in ['message', 'compound']:
                    attribute_value = cmds.getAttr('{}.{}'.format(node, attr))
                    print("{} = {}".format(attr, attribute_value))


if __name__ == '__main__':
    main()
=======

    for node in all_nodes:
        print("Attributes for {}".format(node))
        attribute_list = cmds.listAttr(node)

        for attr in attribute_list:

            if attr != 'message':
                attribute_value = cmds.getAttr('{}.{}'.format(node, attr))

                print("{} = {}".format(attr, attribute_value))


if __name__ == '__main__':
    main()
>>>>>>> dd39bd6b508171453c9dc36e90b2d4418283fbb7
