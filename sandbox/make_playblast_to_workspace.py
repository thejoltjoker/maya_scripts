import maya.cmds as cmds
import os


def playblast():

    cmds.file(sn=True, q=True)
    scene_path, scene_name = os.path.split(cmds.file(sn=True, q=True))
    print scene_path, scene_name

    scene_name = os.path.splitext(scene_name)[0]
    print scene_name

    out_path = os.path.abspath(
        os.path.join(
            scene_path,
            'playblast',
            scene_name
        )
    )

    print out_path

    # if not os.path.exists(os.path.basename(out_path)):
    #     os.makedirs(out_path)

    # playblast  -format image -filename "E:/Dropbox/projects/2018/0100_seq_kabam/3d/sequences/KBL001/010/anim/work/maya/playblast/kabam_KBL001_010_anim_v036/kabam_KBL001_010_anim_v036" -sequenceTime 0 -clearCache 1 -viewer 0 -showOrnaments 0 -fp 4 -percent 100 -compression "png" -quality 100 -widthHeight 1920 1080;
    cmds.playblast(fmt='image',
                   compression='png',
                   filename=os.path.join(out_path, scene_name),
                   orn=False,
                   v=False,
                   percent=100,
                   quality=100,
                   width=1920,
                   height=1080,
                   fo=True
                   )


if __name__ == "__main__":
    playblast()
