#!/usr/bin/env python
"""
copy_attributes.py
Copy all attributes and their respective values, for selected object. Disregards attribute types: message, compound.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    nodes = cmds.ls(sl=True)
    source = nodes[0]
    dest = nodes[1]

    attribute_list = cmds.listAttr(source)
    for attr in attribute_list:
        if '.' not in attr:
            attribute_type = cmds.attributeQuery(attr, node=source, at=True)
            if attribute_type not in ['message', 'compound']:
                attribute_value = cmds.getAttr('{}.{}'.format(source, attr))
                print("{} = {}".format(attr, attribute_value))
                try:
                    cmds.setAttr('{}.{}'.format(dest, attr))
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    main()
