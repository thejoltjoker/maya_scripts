#!/usr/bin/env python
"""redshift_aovs.py
Check for redshift aovs in scene and delete them.
"""
from maya import cmds
import logging

TITLE = 'Redshift AOVs'
CATEGORY = 'Node'
DESCRIPTION = 'Check for existing Redshift AOVs. Fix is to remove them.'

logger = logging.getLogger('Validation')


def check(*args):
    logger.info('Attempting to check {}'.format(TITLE))
    nodes = cmds.ls(type='RedshiftAOV')
    for n in nodes:
        logger.info('{0}: {1}'.format(cmds.getAttr(n + '.aovType'), n))
    return nodes, len(nodes), 0


def fix(*args):
    logger.info('Attempting to fix {}'.format(TITLE))
    nodes = cmds.ls(type='RedshiftAOV')
    nodes.extend(cmds.ls('rsAOVControl'))
    cmds.delete(nodes)


def main():
    """docstring for main"""
    window = cmds.window(title=TITLE)
    cmds.columnLayout()
    cmds.text('Check for redshift aovs.\nFix: Remove aovs')
    cmds.button(label='Check', command=check)
    cmds.button(label='Fix', command=fix)
    cmds.setParent('..')
    cmds.showWindow(window)


if __name__ == '__main__':
    main()
