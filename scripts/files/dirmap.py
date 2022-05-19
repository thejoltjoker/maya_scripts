import sys

from maya import cmds


def main():
    win_path = 'L:/'
    mac_path = '/Users/johannes/frank/libraries/'
    cmds.dirmap(en=True)
    if sys.platform == 'darwin':
        cmds.dirmap(m=(win_path, mac_path))
    else:
        cmds.dirmap(m=(mac_path, win_path))
    print(win_path, '=', cmds.dirmap(cd=win_path))
    print(mac_path, '=', cmds.dirmap(cd=mac_path))


if __name__ == '__main__':
    main()
