#!/usr/bin/env python
"""dof_on_camera.py
Check if dof is enabled on camera and disable it to avoid accidentally rendering with dof.
"""
from maya import cmds
import logging

TITLE = 'DoF on cameras'
CATEGORY = 'Node'
DESCRIPTION = 'Check for existing Redshift AOVs. Fix is to remove them.'

logger = logging.getLogger('Validation')


def check(*args):
    logger.info('Attempting to check {}'.format(TITLE))
    nodes = [x for x in cmds.ls(cameras=True) if cmds.getAttr(x + '.depthOfField')]
    for n in nodes:
        logger.info('{1}: {0}'.format(cmds.getAttr(n + '.depthOfField'), n))
    return nodes, len(nodes), 0


def fix(*args):
    logger.info('Attempting to fix {}'.format(TITLE))
    nodes = [x for x in cmds.ls(cameras=True) if cmds.getAttr(x + '.depthOfField')]
    for n in nodes:
        cmds.setAttr(n + '.depthOfField', 0)
        logger.info('{1}: {0}'.format(cmds.getAttr(n + '.depthOfField'), n))


def main():
    """docstring for main"""
    window = cmds.window(title=TITLE)
    cmds.columnLayout()
    cmds.text('Check for cameras that have DoF enabled.\nFix: Disable DoF')
    cmds.button(label='Check', command=check)
    cmds.button(label='Fix', command=fix)
    cmds.setParent('..')
    cmds.showWindow(window)


if __name__ == '__main__':
    main()
