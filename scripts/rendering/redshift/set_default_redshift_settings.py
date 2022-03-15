#!/usr/bin/env python
"""
set_default_redshift_settings.py
Description of set_default_redshift_settings.py.
"""
import maya.cmds as cmds
import maya.mel as mel


def set_default_settings():
    filename_prefix = '<Scene>/<RenderLayer>/<camera>_<RenderLayer>'
    # mel.eval('unifiedRenderGlobalsWindow')

    # List the plugins that are currently loaded
    plugins = cmds.pluginInfo(query=True, listPlugins=True)
    # Load Redshift
    if not 'redshift4maya' in plugins:
        cmds.loadPlugin('redshift4maya')

    if cmds.getAttr('defaultRenderGlobals.currentRenderer') != 'redshift':
        cmds.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')
        cmds.warning('Redshift was set as current renderer')

    mel.eval('redshiftGetRedshiftOptionsNode(true)')

    # File settings
    cmds.setAttr('redshiftOptions.imageFormat', 1)
    # cmds.setAttr('redshiftOptions.noSaveImage', 1)
    cmds.setAttr('redshiftOptions.exrMultipart', 0)
    cmds.setAttr('redshiftOptions.exrForceMultilayer', 0)
    cmds.setAttr('defaultRenderGlobals.ifp', filename_prefix, type='string')

    # Animation settings
    end_frame = cmds.playbackOptions(q=True, max=True)
    start_frame = cmds.playbackOptions(q=True, min=True)
    cmds.setAttr('defaultRenderGlobals.animation', 1)
    cmds.setAttr('defaultRenderGlobals.byFrameStep', 1)
    cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)
    cmds.setAttr('defaultRenderGlobals.startFrame', start_frame)
    cmds.setAttr('defaultRenderGlobals.endFrame', end_frame)

    # Output settings
    cmds.setAttr('defaultResolution.width', 1920)
    cmds.setAttr('defaultResolution.height', 1080)
    cmds.setAttr('defaultResolution.deviceAspectRatio', 1.777)
    cmds.setAttr('defaultResolution.pixelAspect', 1)

    # Lights
    cmds.setAttr('defaultRenderGlobals.enableDefaultLight', 0)
    cmds.setAttr('redshiftOptions.GIEnabled', 1)

    # Sampler settings
    cmds.setAttr('redshiftOptions.autoProgressiveRenderingIprEnabled', 1)
    cmds.setAttr('redshiftOptions.unifiedRandomizePattern', 1)
    cmds.setAttr('redshiftOptions.enableAutomaticSampling', 0)

    # Motion blur settings
    cmds.setAttr('redshiftOptions.motionBlurEnable', 1)
    cmds.setAttr('redshiftOptions.motionBlurFrameDuration', 0.5)
    cmds.setAttr('redshiftOptions.motionBlurShutterStart', 0.25)
    cmds.setAttr('redshiftOptions.motionBlurShutterEnd', 0.75)
    cmds.setAttr('redshiftOptions.motionBlurShutterEfficiency', 1)
    cmds.setAttr('redshiftOptions.motionBlurDeformationEnable', 1)


def main():
    set_default_settings()


if __name__ == '__main__':
    main()
