"""
create_playblast.py
Description of create_playblast.py.
"""
import os
import sys
from datetime import datetime

from maya import cmds


def playblast(*args, **kwargs):
    scene_path, scene_name = os.path.split(cmds.file(sn=True, q=True))
    today = datetime.today().strftime('%y%m%d')
    new_dailies_folder = os.path.abspath(os.path.join(scene_path, '..', 'playblast', today))

    if not os.path.exists(new_dailies_folder):
        os.makedirs(new_dailies_folder)

    filename = '_'.join([today, os.path.splitext(scene_name)[0]])
    out_file = os.path.join(new_dailies_folder, filename)
    out_file = os.path.abspath("{0}.mov".format(out_file))
    print(out_file)
    params = {'filename': out_file,
              'clearCache': True,
              'fmt': 'qt',
              'orn': False,
              'v': False,
              'percent': 100,
              'quality': 100,
              'width': 1920,
              'height': 1080,
              'fo': True
              }
    if sys.platform == 'win32':
        params['compression'] = 'Animation'
    else:
        params['compression'] = 'h264'
    cmds.playblast(**params)
    cmds.warning("{0} created in {1}".format(filename, new_dailies_folder))


def main():
    """docstring for main"""
    playblast()


if __name__ == '__main__':
    main()
