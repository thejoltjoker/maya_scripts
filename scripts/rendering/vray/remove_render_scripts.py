#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
remove_render_scripts.py
Description of remove_render_scripts.py.
"""
import maya.cmds as cmds


def main():
    """docstring for main"""
    settings = ['defaultRenderGlobals.preMel',
                'defaultRenderGlobals.postMel',
                'defaultRenderGlobals.preRenderLayerMel',
                'defaultRenderGlobals.postRenderLayerMel',
                'defaultRenderGlobals.preRenderMel',
                'defaultRenderGlobals.postRenderMel',
                'vraySettings.preKeyframeMel',
                'vraySettings.rtImageReadyMel'
                ]
    for field in settings:
        cmds.setAttr(field, '', type='string')

    mel.eval('SubmitJobToDeadline')


if __name__ == '__main__':
    main()
