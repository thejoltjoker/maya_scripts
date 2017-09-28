#!/usr/bin/env python
"""
list_attributes.py
Description of list_attributes.py.
"""


def main():
    """docstring for main"""
    all_nodes = cmds.ls(sl=True)

    for node in all_nodes:
        print("Attributes for {}".format(node))
        attribute_list = cmds.listAttr(node)

        for attr in attribute_list:

            if attr != 'message':
                attribute_value = cmds.getAttr('{}.{}'.format(node, attr))

                print("{} = {}".format(attr, attribute_value))


if __name__ == '__main__':
    main()