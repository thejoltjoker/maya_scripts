#!/usr/bin/env python
"""redshift_aovs.py
Check for redshift aovs in scene and delete them.
"""
from maya import cmds
import logging

TITLE = 'Unknown Nodes'
CATEGORY = 'Node'
DESCRIPTION = 'Check for unknown nodes in scenes and remove them'

logger = logging.getLogger('Validation')


def check(*args):
    logger.info('Attempting to check {}'.format(TITLE))

    unknown_nodes = cmds.ls(type='unknown', l=True)
    for n in unknown_nodes:
        logger.info('Unknown node "{}"'.format(n))
    return unknown_nodes, len(unknown_nodes), 0


def fix(*args):
    logger.info('Attempting to fix {}'.format(TITLE))
    unknown_nodes = check()
    for n in unknown_nodes[0]:
        if cmds.objExists(n):
            cmds.lockNode(n, l=False)
            cmds.delete(n)
            logger.info('Deleted unknown node "{}"'.format(n))


def main():
    """docstring for main"""
    window = cmds.window(title=TITLE)
    cmds.columnLayout()
    cmds.text(DESCRIPTION)
    cmds.button(label='Check', command=check)
    cmds.button(label='Fix', command=fix)
    cmds.setParent('..')
    cmds.showWindow(window)


if __name__ == '__main__':
    main()
