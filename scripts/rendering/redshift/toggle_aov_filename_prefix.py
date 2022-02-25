#!/usr/bin/env python
"""
toggle_aov_filename_prefix.py

Set the file name prefix of redshift AOVs.
"""
import maya.cmds as cmds

EXCLUDE = ['Cryptomatte', 'Depth']


def set_filename_prefix(prefix='<BeautyPath>/<BeautyFile>.<RenderPass>', exclude=None):
    if not exclude:
        exclude = []

    nodes = cmds.ls(type='RedshiftAOV')

    for aov in nodes:
        if not cmds.getAttr(aov + '.aovType') in exclude:
            cmds.setAttr(aov + ".filePrefix", prefix, type='string')
            print(aov + " prefix is now %s" % prefix)

    cmds.warning("AOVs prefixes have been set to %s" % prefix)


def main():
    dialog = cmds.confirmDialog(title='Change aov prefix', message='Do you want multichannel exr?',
                                button=['Yes', 'No'],
                                defaultButton='Yes',
                                cancelButton='No')
    if dialog == 'Yes':
        set_filename_prefix(prefix='<BeautyPath>/<BeautyFile>', exclude=EXCLUDE)
    elif dialog == 'No':
        set_filename_prefix()


if __name__ == '__main__':
    main()
