"""enable_proxy_visibility_override.py
Description of enable_proxy_visibility_override.py.
"""
from maya import cmds


def main():
    """docstring for main"""
    for node in cmds.ls(type='RedshiftProxyMesh'):
        cmds.setAttr(node + ".visibilityMode", 1)


if __name__ == '__main__':
    main()
