"""export_camera_nuke.py
Export the selected or active camera to nuke.
"""
import os
from maya import cmds


def get_cameras():
    """Get the correct camera based on selection or viewport

    Returns:
        list: list of camera transform nodes
    """
    cameras = []

    # Check if any cameras are selected and use those
    nodes = cmds.ls(sl=True)
    for node in nodes:
        # If camera shape selected
        if cmds.nodeType(node) == 'camera':
            cameras.append(cmds.listRelatives(p=True)[0])

        # Iterate over shapes
        else:
            shapes = cmds.listRelatives(node)
            for s in shapes:
                if cmds.nodeType(s) == 'camera':
                    cameras.append(node)

    # Get renderable cameras if no cameras are selected
    if not cameras:
        nodes = cmds.ls(ca=True)
        for node in nodes:
            if cmds.getAttr(node + '.renderable'):
                cameras.append(cmds.listRelatives(p=True))

    return cameras


def frame_range():
    """Get the maximum frame range of the current scene.
    Checks defaultRenderGlobals, time slider and animation timeline.

    Returns:
        tuple: (start, end)
    """
    # Get range from defaultRenderGlobals
    render_globals_start = cmds.getAttr('defaultRenderGlobals.startFrame')
    render_globals_end = cmds.getAttr('defaultRenderGlobals.endFrame')

    # Get range from time slider
    time_slider_start = cmds.playbackOptions(q=True, min=True)
    time_slider_end = cmds.playbackOptions(q=True, max=True)

    # Get range from timeline
    timeline_start = cmds.playbackOptions(q=True, ast=True)
    timeline_end = cmds.playbackOptions(q=True, aet=True)

    # Get the smallest and largest to make sure the entire animation is included
    start_frame = min(render_globals_start, time_slider_start, timeline_start)
    end_frame = max(render_globals_end, time_slider_end, timeline_end)

    return start_frame, end_frame


def clone_camera(camera, suffix='clone'):
    """Make a duplicate of the camera

    Args:
        camera (transform): the transform node for a camera

    Returns:
        string: the duplicated camera
    """
    # Duplicate camera and parent to world
    clone = cmds.duplicate(camera, n=camera + '_' + suffix)[0]
    cmds.parent(clone, w=True)

    # Constrain to original camera
    cmds.parentConstraint(camera, clone, mo=False)

    return clone


def bake_animation(node, start_frame, end_frame):
    """Bake animation of a node

    Returns:
        node: same as input
    """
    params = {
        'simulation': True,
        't': (start_frame, end_frame),
        'sampleBy': 1,
        'disableImplicitControl': True
    }

    cmds.bakeResults(node, **params)

    return node


def export_fbx(nodes, path, start_frame, end_frame):
    """Export given nodes as an fbx file for nuke

    Args:
        nodes: list of nodes/cameras
        path: output path

    Returns:
        str(path)
    """
    cmds.select(nodes)

    # Setup export
    cmds.FBXExportCameras('-v', True)
    cmds.FBXExportBakeComplexAnimation('-v', True)
    cmds.FBXExportBakeComplexStart('-v', int(start_frame))
    cmds.FBXExportBakeComplexEnd('-v', int(end_frame))
    cmds.FBXExportFileVersion('-v', 'FBX200611')

    # Export
    cmds.FBXExport('-f', path, '-s')

    return path


def cameras_to_nuke():
    """Export selected/renderable cameras for use in nuke"""
    start_frame, end_frame = frame_range()

    # Get cameras and bake them
    cameras = get_cameras()
    print('Baking animation for '+', '.join(cameras))
    baked_cameras = []
    for cam in cameras:
        clone = clone_camera(cam, suffix='baked')
        baked_cameras.append(bake_animation(clone, start_frame, end_frame))

    # Output path
    scene_path, scene_name = os.path.split(cmds.file(sn=True, q=True))
    output_path = os.path.abspath(os.path.join(scene_path, '..', 'cameras'))
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    filename = '_'.join([os.path.splitext(scene_name)[0], 'cameras']) + '.fbx'
    output_path = os.path.join(output_path, filename)

    # Export
    export_fbx(baked_cameras, output_path, start_frame, end_frame)
    cmds.warning(', '.join(baked_cameras)+' exported to '+output_path)


def main():
    cameras_to_nuke()


if __name__ == '__main__':
    main()
