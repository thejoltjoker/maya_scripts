#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
incremental_save.py
Description of incremental_save.py.
"""
import maya.standalone
import maya.cmds as cmds
import os
import re


def main():
    maya.standalone.initialize()
    cmds.file(r'E:\Dropbox\projects\2018\0100_seq_kabam\3d\sequences\KBL001\010\light\work\maya\kabam_KBL001_010_light_v015.ma', open=True)
    # cmds.file('C:/Users/thejoltjoker/Desktop/test_scene_v001.ma', open=True)
    # cmds.showHidden(['MASH_L_DEST_ReproMesh',
    #                  'MASH_R_DEST_ReproMesh',
    #                  'MASH_FLOAT_DEST_ReproMesh'])

    cmds.sets(['KBL001_010_anim:MASH_L_DEST_ReproMesh',
               'KBL001_010_anim:MASH_R_DEST_ReproMesh',
               'KBL001_010_anim:MASH_FLOAT_DEST_ReproMesh'],
              e=True,
              forceElement='butterfly_MAIN_SG')

    # Save file
    cmds.file(save=True)
    maya.standalone.uninitialize()


if __name__ == '__main__':
    main()
