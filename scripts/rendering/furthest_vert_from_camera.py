#!/usr/bin/env python3
"""furthest_vert_from_camera.py
Description of furthest_vert_from_camera.py.
"""
import math

from maya import cmds
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def magnitude(vec):
    summ = 0
    for i in range(len(vec)):
        summ = vec[i] * vec[i] + summ
    return pow(summ, 0.5)


def distance_between(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2))


def active_camera():
    panel = cmds.getPanel(withFocus=True)
    cam_shape = cmds.modelEditor(panel, q=1, av=1, cam=1)

    if cmds.listRelatives(cam_shape, p=True):
        return cmds.listRelatives(cam_shape, p=True)[0]
    return None


def world_position(node):
    return cmds.xform(node, q=True, ws=True, rp=True)


def all_geo_transforms():
    transforms = []
    nodes = cmds.ls(geometry=True)

    for node in nodes:
        parent = cmds.listRelatives(node, p=True)
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

    furthest_away = max(distances, key=lambda item: item[1])
    return furthest_away


def main():
    """docstring for main"""
    # Get camera position
    camera = active_camera()
    camera_pos = world_position(camera)
    logger.info(f'Active camera is {camera}')
    logger.info(f'Camera position is {camera_pos}')

    # Get object furthest from camera
    objects = all_geo_transforms()
    furthest_object = furthest_transform_from_transform(camera, objects)
    logger.info(f'Furthest vertex is {furthest_object[0]} at a distance of {furthest_object[1]}')

    # Get vertex furthest from camera
    verts = cmds.ls(furthest_object[0] + '.vtx[*]', fl=1)
    furthest_vert = furthest_vertex_from_transform(camera, verts)
    logger.info(f'Furthest vertex is {furthest_vert[0]} at a distance of {furthest_vert[1]}')


if __name__ == '__main__':
    main()
