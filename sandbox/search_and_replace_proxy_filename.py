#!/usr/bin/env python
"""
search_and_replace_proxy_filename.py
Description of search_and_replace_proxy_filename.py.
"""

import maya.cmds as cmds

SEARCH_STRING = 'D:/The Sequence Group//assets/vrayProxy'
REPLACE_STRING = '//SEQ-LIVE/live_projects/ConcordSaison/assets/Environment/Patio/Model/work/maya/vrayProxy'


def main():
    """docstring for main"""
    all_nodes = cmds.ls(sl=True)
    for node in all_nodes:
        if cmds.nodeType(node) == 'VRayMesh':
            old_path = cmds.getAttr('{}.fileName2'.format(node))
            new_path = old_path.replace(SEARCH_STRING, REPLACE_STRING)
            print new_path
            cmds.setAttr('{}.fileName2'.format(node), new_path, type="string")


if __name__ == '__main__':
    main()