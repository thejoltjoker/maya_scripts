#!/usr/bin/env python
"""redshift_aovs.py
Description of redshift_aovs.py.
"""
import math

from maya import cmds, mel
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

AOVS_BEAUTY_AND_RAW = ['Specular Lighting',
                       'Reflections',
                       'Refractions',
                       'Emission']

AOVS_BEAUTY = ['Diffuse Lighting',
               'Sub Surface Scatter',
               'Global Illumination',
               'Caustics']
AOVS_BEAUTY.extend(AOVS_BEAUTY_AND_RAW)

AOVS_BEAUTY_RAW = ['Diffuse Filter',
                   'Diffuse Lighting Raw',
                   'Global Illumination Raw',
                   'Sub Surface Scatter Raw',
                   'Caustics Raw']
AOVS_BEAUTY_RAW.extend(AOVS_BEAUTY_AND_RAW)

AOVS_UTIL = ['Bump Normals',
             'Cryptomatte',
             'Depth',
             # 'Motion Vectors',
             'Normals',
             'World Position',
             'Ambient Occlusion']


def renderer_is_redshift():
    if cmds.getAttr("defaultRenderGlobals.currentRenderer") != 'redshift':
        cmds.warning("Redshift is not current renderer")
        return False
    else:
        return True


def set_redshift_renderer():
    # List the plugins that are currently loaded
    plugins = cmds.pluginInfo(query=True, listPlugins=True)

    # Load Redshift
    if 'redshift4maya' in plugins:
        print('Redshift is already loaded.')
    else:
        try:
            cmds.loadPlugin('redshift4maya')
            print('Redshift is now loaded.')
        except Exception as e:
            print(e)
            return
    # Set renderer
    cmds.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')
    cmds.warning('Renderer set to Redshift')


def create_redshift_aovs(aov_names, color_processing=True):
    """Create redshift aov nodes"""
    existing_aovs = {aov_nice_name(x): x for x in cmds.ls(type='RedshiftAOV', l=True)}
    aov_nodes = []
    for aov in aov_names:
        if existing_aovs.get(aov):
            aov_node = existing_aovs.get(aov)
        else:
            if aov == 'Depth':
                aov_node = create_depth_aov()
            elif aov == 'Ambient Occlusion':
                aov_node = create_ao_aov()
            else:
                aov_node = cmds.rsCreateAov(type=aov)
                mel.eval('redshiftUpdateActiveAovList()')
        if color_processing:
            attr_exist = cmds.attributeQuery('applyColorProcessing', node=aov_node, exists=True)
            if attr_exist:
                cmds.setAttr(aov_node + '.applyColorProcessing', 0)
        aov_nodes.append(aov_node)

    # Update ui
    mel.eval('redshiftUpdateActiveAovList')
    return aov_nodes


def aov_nice_name(node):
    return cmds.getAttr(node + '.aovType')


def create_redshift_beauty_aovs():
    aovs = create_redshift_aovs(AOVS_BEAUTY)
    return aovs


def create_redshift_raw_beauty_aovs():
    aovs = create_redshift_aovs(AOVS_BEAUTY_RAW)
    return aovs


def create_redshift_util_aovs():
    aovs = create_redshift_aovs(AOVS_UTIL)
    return aovs


def create_aov_switch():
    if renderer_is_redshift():
        # Create beauty AOVs
        beauty = create_redshift_beauty_aovs()

        # Create raw beauty AOVs
        # raw_beauty = create_redshift_raw_beauty_aovs()

        # Create Utility AOVs
        utils = create_redshift_util_aovs()

        # Create pass holder
        pass_holder = cmds.polyCube(n='rsPassAttrHolder')[0]
        cmds.setAttr(pass_holder + '.visibility',
                     0, k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.tx', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.ty', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.tz', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.rx', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.ry', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.rz', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.sx', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.sy', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder + '.sz', k=False, l=True, cb=False)
        cmds.delete(pass_holder, ch=True)

        # Create pass holder group
        pass_holder_grp = cmds.group(pass_holder, name='rsAOVControl')
        cmds.setAttr(pass_holder_grp + '.visibility', 1, k=False, cb=False)
        cmds.setAttr(pass_holder_grp + '.tx', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.ty', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.tz', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.rx', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.ry', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.rz', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.sx', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.sy', k=False, l=True, cb=False)
        cmds.setAttr(pass_holder_grp + '.sz', k=False, l=True, cb=False)
        cmds.delete(pass_holder_grp, ch=True)
        cmds.addAttr(pass_holder_grp, ln='enableBeauty', nn='Enable Beauty AOVs', at='bool', dv=1, k=True)
        # cmds.addAttr(pass_holder_grp, ln='enableRawBeauty', nn='Enable Raw Beauty AOVs', at='bool', dv=0, k=True)
        cmds.addAttr(pass_holder_grp, ln='enableRefractions', nn='Refractions', at='bool', dv=0, k=True)
        cmds.addAttr(pass_holder_grp, ln='enableEmission', nn='Emission', at='bool', dv=0, k=True)
        cmds.addAttr(pass_holder_grp, ln='enableSSS', nn='SSS', at='bool', dv=0, k=True)
        cmds.addAttr(pass_holder_grp, ln='enableUtility', nn='Enable Utility AOVs', at='bool', dv=1, k=True)

        # Connect attributes
        existing_aovs = cmds.ls(type='RedshiftAOV', l=True)
        for aov_node in existing_aovs:
            aov_nice = aov_nice_name(aov_node)
            if aov_nice in AOVS_BEAUTY:
                if aov_nice == 'Refractions':
                    cmds.connectAttr(pass_holder_grp + '.enableRefractions', aov_node + '.enabled', )

                elif aov_nice == 'Caustics':
                    cmds.connectAttr(pass_holder_grp + '.enableRefractions', aov_node + '.enabled')

                elif aov_nice == 'Caustics Raw':
                    cmds.connectAttr(pass_holder_grp + '.enableRefractions', aov_node + '.enabled')

                elif aov_nice == 'Emission':
                    cmds.connectAttr(pass_holder_grp + '.enableEmission', aov_node + '.enabled')

                elif aov_nice == 'Sub Surface Scatter':
                    cmds.connectAttr(pass_holder_grp + '.enableSSS', aov_node + '.enabled')
                else:
                    # Connect attributes
                    cmds.connectAttr(pass_holder_grp + '.enableBeauty', aov_node + '.enabled')

            elif aov_nice in AOVS_BEAUTY_AND_RAW:
                # Create blend colors node
                mult_div_node = cmds.shadingNode('blendColors', n=aov_node + '_BLEND', asUtility=True)

                # Connect attributes
                # cmds.connectAttr(pass_holder_grp + '.enableRawBeauty', mult_div_node + '.color1R')
                cmds.connectAttr(pass_holder_grp + '.enableBeauty', mult_div_node + '.color2R')
                cmds.connectAttr(mult_div_node + '.outputR',
                                 aov_node + '.enabled')
            # elif aov_nice in AOVS_BEAUTY_RAW:
            #     cmds.connectAttr(pass_holder_grp + '.enableRawBeauty', aov_node + '.enabled')
            elif aov_node in utils:

                cmds.connectAttr(pass_holder_grp + '.enableUtility', aov_node + '.enabled', f=True)


            else:
                print(aov_nice + " was created manually and was not assigned to the AOV control.")

        cmds.select(pass_holder_grp)
        return pass_holder_grp


def create_ao_aov():
    """Create a custom aov with an ambient occlusion shader.
    """
    # Create custom aov
    aov_node = cmds.rsCreateAov(type='Custom', name='rsAov_AmbientOcclusion')
    cmds.setAttr(aov_node + '.name', 'Ambient Occlusion', type='string')

    # Update aov list
    mel.eval('redshiftUpdateActiveAovList()')

    # Create ambient occlusion material
    material = cmds.shadingNode('RedshiftAmbientOcclusion', name='ambientOcclusion_shd', asUtility=True)

    # Connect material to aov
    cmds.connectAttr('{}.outColor'.format(material), '{}.defaultShader'.format(aov_node), f=True)

    return aov_node


def create_depth_aov():
    """Create a custom aov with an ambient occlusion shader.
    """
    max_depth = zdepth_distance()
    # Create custom aov
    aov_node = cmds.rsCreateAov(type='Depth')
    cmds.setAttr(aov_node + '.depthMode', 1)
    cmds.setAttr(aov_node + '.useCameraNearFar', 0)
    cmds.setAttr(aov_node + '.maxDepth', max_depth)

    return aov_node


def distance_between(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2))


def active_camera():
    camera = 'persp'
    try:
        panel = cmds.getPanel(withFocus=True)
        cam_shape = cmds.modelEditor(panel, q=1, av=1, cam=1)

        if cmds.listRelatives(cam_shape, p=True):
            camera = cmds.listRelatives(cam_shape, p=True)[0]
    except Exception as e:
        render_cams = renderable_cameras()
        if render_cams:
            camera = render_cams[0]

    return camera


def world_position(node):
    return cmds.xform(node, q=True, ws=True, rp=True)


def all_geo_transforms():
    transforms = []
    nodes = cmds.ls(geometry=True, l=True)

    for node in nodes:
        parent = cmds.listRelatives(node, p=True, pa=True)
        for p in parent:
            transforms.append(p)
    return transforms


def furthest_transform_from_transform(target, nodes):
    distances = []
    target_pos = world_position(target)
    for node in nodes:
        world_pos = world_position(node)

        # Get distance from target
        distance_from_target = distance_between(target_pos, world_pos)
        distances.append((node, distance_from_target))

    furthest_away = max(distances, key=lambda item: item[1])
    return furthest_away


def furthest_vertex_from_transform(target, vertices):
    distances = []
    target_pos = world_position(target)
    for v in vertices:
        ppos = cmds.pointPosition(v)

        # Get distance from target
        distance_from_target = distance_between(target_pos, ppos)
        distances.append((v, distance_from_target))

        logger.info(v)
        logger.info(ppos)
        logger.info(distance_from_target)
        logger.info(distances)
    furthest_away = max(distances, key=lambda item: item[1])
    return furthest_away


def renderable_cameras():
    """Check for renderable cameras"""
    renderable_cameras = []
    cameras = cmds.ls(ca=True, l=True)
    for cam in cameras:
        if cmds.getAttr("{}.renderable".format(cam)):
            cam_parent = cmds.listRelatives(cam, parent=True)
            renderable_cameras.append(cam_parent[0])

    return renderable_cameras


def zdepth_distance():
    """docstring for main"""
    distance = 1000
    # Get camera position
    camera = active_camera()
    camera_pos = world_position(camera)
    logger.info(f'Active camera is {camera}')
    logger.info(f'Camera position is {camera_pos}')

    # Get object furthest from camera
    objects = all_geo_transforms()
    if objects:
        furthest_object = furthest_transform_from_transform(camera, objects)
        logger.info(f'Furthest vertex is {furthest_object[0]} at a distance of {furthest_object[1]}')

        # Get vertex furthest from camera
        verts = cmds.ls(furthest_object[0] + '.vtx[*]', fl=1)
        if verts:
            furthest_vert = furthest_vertex_from_transform(camera, verts)
            logger.info(f'Furthest vertex is {furthest_vert[0]} at a distance of {furthest_vert[1]}')
            distance = furthest_vert[1] * 1.25
        else:
            distance = furthest_object[1] * 1.25
    return distance


def main():
    print(zdepth_distance())
    create_aov_switch()
    # if not renderer_is_redshift():
    #     confirmation = cmds.confirmDialog(title='Set render engine',
    #                                       message='Do you want to set Redshift as render engine?', button=['Yes', 'No'],
    #                                       defaultButton='Yes',
    #                                       cancelButton='No', dismissString='No')
    #     if confirmation == 'Yes':
    #         set_redshift_renderer()
    #     else:
    #         cmds.warning('Redshift is not the current render engine')
    #         return
    # create_aov_switch()


if __name__ == '__main__':
    main()
