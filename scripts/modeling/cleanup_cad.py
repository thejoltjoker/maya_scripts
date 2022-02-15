#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
script_name.py
Description of script_name.py.
Credit to https://www.akeric.com/blog/?p=1087 for uninstance function.
"""
import logging
import os
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

SUFFIXES = {'RedshiftCurvature': 'rsCurvature',
            'RedshiftMatteParameters': 'rsMatteParameters',
            'RedshiftCurveSet': 'rsCurveSet',
            'RedshiftDomeLight': 'lgt',
            'RedshiftIESLight': 'lgt',
            'RedshiftMeshParameters': 'rsMeshParameters',
            'RedshiftObjectId': 'rsObjectId',
            'RedshiftOptions': 'RedshiftOptions',
            'RedshiftPhysicalLight': 'lgt',
            'RedshiftPortalLight': 'lgt',
            'RedshiftPostEffects': 'rsPostEffects',
            'RedshiftTraceSet': 'rsTraceSet',
            'RedshiftVisibility': 'rsVisibility',
            'RedshiftVolumeShape': 'rsVolumeShape',
            'ambientLight': 'lgt',
            'areaLight': 'lgt',
            'camera': 'cam',
            'colorManagementGlobals': 'colorManagementGlobals',
            'defaultLightList': 'defaultLightList',
            'defaultRenderUtilityList': 'defaultRenderUtilityList',
            'defaultRenderingList': 'defaultRenderingList',
            'defaultShaderList': 'defaultShaderList',
            'defaultTextureList': 'defaultTextureList',
            'directionalLight': 'lgt',
            'displayLayer': 'displayLayer',
            'displayLayerManager': 'displayLayerManager',
            'dof': 'dof',
            'dynController': 'dynController',
            'globalCacheControl': 'globalCacheControl',
            'group': 'grp',
            'hardwareRenderGlobals': 'hardwareRenderGlobals',
            'hardwareRenderingGlobals': 'hardwareRenderingGlobals',
            'hikSolver': 'hikSolver',
            'hwRenderGlobals': 'hwRenderGlobals',
            'hyperGraphInfo': 'hyperGraphInfo',
            'hyperLayout': 'hyperLayout',
            'ikRPsolver': 'ikRPsolver',
            'ikSCsolver': 'ikSCsolver',
            'ikSplineSolver': 'ikSplineSolver',
            'ikSystem': 'ikSystem',
            'lambert': 'lambert',
            'lightLinker': 'lightLinker',
            'lightList': 'lightList',
            'locator': 'locator',
            'lookAt': 'lookAt',
            'makeNurbSphere': 'makeNurbSphere',
            'materialInfo': 'materialInfo',
            'mesh': 'geo',
            'nurbsCurve': 'crv',
            'nurbsSurface': 'nurbsSurface',
            'objectMultiFilter': 'objectMultiFilter',
            'objectNameFilter': 'objectNameFilter',
            'objectSet': 'objectSet',
            'particleCloud': 'particleCloud',
            'partition': 'partition',
            'pointLight': 'lgt',
            'polySphere': 'polySphere',
            'poseInterpolatorManager': 'poseInterpolatorManager',
            'postProcessList': 'postProcessList',
            'renderGlobals': 'renderGlobals',
            'renderGlobalsList': 'renderGlobalsList',
            'renderLayer': 'renderLayer',
            'renderLayerManager': 'renderLayerManager',
            'renderQuality': 'renderQuality',
            'renderSphere': 'renderSphere',
            'resolution': 'resolution',
            'sequenceManager': 'sequenceManager',
            'shaderGlow': 'shaderGlow',
            'shadingEngine': 'shadingEngine',
            'shapeEditorManager': 'shapeEditorManager',
            'spotLight': 'lgt',
            'standardSurface': 'standardSurface',
            'strokeGlobals': 'strokeGlobals',
            'time': 'time',
            'RedshiftMaterial': 'shd',
            'transform': 'transform',
            'viewColorManager': 'viewColorManager',
            'volumeFog': 'volumeFog',
            'volumeLight': 'lgt'}


def get_instances():
    instances = []
    iterDag = om.MItDag(om.MItDag.kBreadthFirst)
    while not iterDag.isDone():
        instanced = om.MItDag.isInstanced(iterDag)
        if instanced:
            instances.append(iterDag.fullPathName())
        iterDag.next()
    return instances


def uninstance():
    instances = get_instances()
    logger.info('Found {0} instances'.format(len(instances)))
    while len(instances):
        parent = cmds.listRelatives(instances[0], parent=True, fullPath=True)[0]
        cmds.duplicate(parent, renameChildren=True)
        cmds.delete(parent)
        instances = get_instances()
    return instances


def get_suffix(node):
    node_type = cmds.nodeType(node)
    if node_type == 'transform':
        node_shapes = cmds.listRelatives(node, s=True, path=True)
        if node_shapes is not None:
            for shape in node_shapes:
                node_type = cmds.nodeType(shape)
        else:
            node_type = 'group'
    return SUFFIXES.get(node_type, node_type)


def increment_name(name, suffix):
    inc = 1
    while True:
        new_name = '{name}{inc:03d}_{suffix}'.format(name=name, inc=inc, suffix=suffix)
        if not cmds.objExists(new_name):
            return new_name
        inc += 1


def clean_name(name):
    return name.replace(' ', '_')


def rename(name, nodes):
    renamed = []
    # Get selection and sort it
    sorted_sel = sorted(nodes, key=len, reverse=True)

    # Clean illegal characters
    name = clean_name(name)

    # Loop through selected objects
    for node in sorted_sel:
        suffix = get_suffix(node)

        if len(sorted_sel) > 1:
            new_name = increment_name(name, suffix)
        else:
            new_name = '_'.join([name, suffix])
            if cmds.objExists(new_name):
                new_name = increment_name(name, suffix)

        # Rename nodes
        renamed_node = cmds.rename(node, new_name)
        renamed.append(renamed_node)
        logger.info('Renamed {0} to {1}'.format(node, renamed_node))

    return renamed


def expand_selection():
    cmds.select(hi=True)
    nodes = cmds.ls(sl=True, dag=True, allPaths=True, long=True)
    logger.info('{} nodes selected'.format(len(nodes)))
    return nodes


def main(name):
    """docstring for main"""
    # Convert instances
    # mel.eval('ConvertInstanceToObject;')
    uninstance()

    # Fix names and rename
    nodes = expand_selection()
    renamed = rename(name, nodes)

    # Select renamed nodes
    cmds.select(renamed)

    # Rename uv set
    logger.info('Renaming UV sets to map1')
    cmds.polyUVSet(rename=True, newUVSet='map1')


if __name__ == '__main__':
    name_dialog = cmds.promptDialog(
        title='Rename',
        message='Enter new name:',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if name_dialog == 'OK':
        name = cmds.promptDialog(query=True, text=True)
        if name:
            main(name)
        else:
            cmds.warning("The name can't be blank")
    else:
        logger.info('User cancelled renaming')
