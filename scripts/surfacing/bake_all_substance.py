"""bake_all_substance.py
Description of bake_all_substance.py.
"""
import os

from maya import cmds, mel


def main():
    """docstring for main"""
    path = os.path.dirname(cmds.file(q=True, exn=True))
    # Substance folder
    if os.path.basename(path) == 'scenes':
        textures_path = os.path.join(path, '..', 'substance')
    else:
        textures_path = os.path.join(path, 'substance')

    textures_path = os.path.abspath(textures_path)

    cmds.select(cmds.ls(type='substanceNode'), replace=True)
    cmd = r'substanceUtilityBakeSelected "%s"' % textures_path
    mel.eval(cmd)


if __name__ == '__main__':
    main()
