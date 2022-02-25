#!/usr/bin/env python
"""
add_aovs_to_multichannel_exr.py

Set the file name prefix of redshift AOVs.
"""
import maya.cmds as cmds


def fix_filename_prefix():
    nodes = cmds.ls(type='RedshiftAOV')
    for aov in nodes:
        if not 'crypto' in aov.lower():
            cmds.setAttr(aov + ".filePrefix", "<BeautyPath>/<BeautyFile>", type='string')
            print(aov + " has been added to multichannel exr.")

    cmds.warning("AOVs have been added to multichannel exr.")


def main():
    fix_filename_prefix()


if __name__ == '__main__':
    main()
