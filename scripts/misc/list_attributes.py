#!/usr/bin/env python
"""
copy_attributes.py
Lists all attributes and their respective values, for selected object. Disregards attribute types: message, compound.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    all_nodes = cmds.ls(sl=True)
    for node in all_nodes:
        print("Attributes for {} ({})".format(node, cmds.nodeType(node)))
        attribute_list = cmds.listAttr(node)
        for attr in attribute_list:
            if not '.' in attr:
                attribute_type = cmds.attributeQuery(attr, node=node, at=True)
                attribute_value = None
                if attribute_type not in ['message', 'compound']:
                    try:
                        attribute_value = cmds.getAttr('{}.{}'.format(node, attr))
                    except:
                        attribute_value = cmds.listAttr('{}.{}'.format(node, attr), multi=True)

                else:
                    print('Attribute type {}'.format(attribute_type))

                if attr and attribute_value:
                    print("{} = {} ({})".format(attr, attribute_value, attribute_type))


if __name__ == '__main__':
    main()
