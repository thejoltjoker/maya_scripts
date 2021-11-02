#!/usr/bin/env python
"""
search_and_replace_proxy_filename.py
Description of search_and_replace_proxy_filename.py.
"""
import maya.cmds as cmds

FINAL_GEO_TYPE = 4


def main():
    """docstring for main"""
    all_nodes = cmds.ls(sl=True)
    for node in all_nodes:
        node_connections = cmds.listConnections(t='VRayMesh')
        if node_connections:
            print node_connections
            for vray_mesh in node_connections:
                print vray_mesh
                if cmds.nodeType(vray_mesh) == 'VRayMesh':
                    cmds.setAttr('{}.geomType'.format(vray_mesh), 0)
                    cmds.setAttr('{}.geomType'.format(vray_mesh),
                                 FINAL_GEO_TYPE)


if __name__ == '__main__':
    main()