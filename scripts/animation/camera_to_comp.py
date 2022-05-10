"""camera_to_comp.py
Description of camera_to_comp.py.
"""
import os.path

from maya import cmds


def bake_camera(camera, frame_range=None):
    """

    Args:
        camera: The camera node
        frame_range (tuple):
    """

    params = {
        'simulation': True,
        'sampleBy': 1,
        'oversamplingRate': 1,
        'disableImplicitControl': True,
        'preserveOutsideKeys': True,
        'sparseAnimCurveBake': True,
        'removeBakedAttributeFromLayer': False,
        'removeBakedAnimFromLayer': False,
        'bakeOnOverrideLayer': False,
        'minimizeRotation': True,
        'controlPoints': False,
        'shape': True
    }
    if frame_range:
        params['t'] = frame_range

    results = cmds.bakeResults(camera, **params)
    return results


def export_fbx(nodes, path):
    cmds.select(nodes)
    cmds.file(path,
              force=True,
              options='v=0;',
              typ='FBX export',
              pr=True,
              es=True)


def main():
    """docstring for main"""
    print(cmds.file(q=True, sn=True))
    # camera = cmds.ls(sl=True)[0]
    # baked = bake_camera(camera, (1, 42))
    # print(baked)
    # file_path = cmds.file(q=True, exn=True)
    # output_path = os.path.dirname()
    # export_fbx(camera, )


if __name__ == '__main__':
    main()
