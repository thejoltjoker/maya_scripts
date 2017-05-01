"""
offset_keyframes.py
"""

import maya.cmds as cmds


# def offset_keyframe(to_frame=1001, delete_shot=False):

#     old_start_frame = mc.getAttr("%s.startFrame" % shot[0])
#     old_end_frame = mc.getAttr("%s.endFrame" % shot[0])
#     frame_offset_value = to_frame-old_start_frame
#     mc.setAttr("%s.startFrame" % shot[0], to_frame)
#     mc.setAttr("%s.endFrame" % shot[0], old_end_frame+frame_offset_value)

# firstKeyframe - animStartFrame * -1

def offset_anim_keyframe(anim_curves, frame_offset):
    cmds.keyframe(anim_curves, e=1, includeUpperBound=True, option='over', relative=1, timeChange=frame_offset)

# offset all keyframes
all_curves = cmds.ls(type="animCurve")
valid_curves = list()
for curve in all_curves:
    is_ref = cmds.referenceQuery(curve, inr=1)
    if not is_ref:
        valid_curves.append(curve)

frame_offset_value = 1

offset_anim_keyframe(valid_curves, frame_offset_value)
