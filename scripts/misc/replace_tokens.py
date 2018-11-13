#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
replace_tokens.py
Description of replace_tokens.py.
"""
import os


def replace_tokens():
    """docstring for replace_tokens"""
    settings = {
        "projects_path": r"E:\Dropbox\rafiki\assets\dirTemplates\vfx",
        "folder_structure": {
            "project_root": "<projects_path>/<project>",
            "asset": "<project>/<discipline>/<assets>/<asset_type>/<asset_name>/<step>",
            #  E: \Dropbox\rafiki\assets\dirTemplates\vfx\0000_projectName\3d\assets\char\assetName\model\work\maya
            "shot": "<project>/<discipline>/<sequences>/<seq_name>/<shot_name>/<step>"
            #  E: \Dropbox\rafiki\assets\dirTemplates\vfx\0000_projectName\3d\sequences\sq001\sh010\light\work\maya
        }
    }
    path = r'E:\Dropbox\rafiki\assets\dirTemplates\vfx\0000_projectName\3d\assets\char\assetName\model\work\maya'.replace(
        '\\', '/').split('/')
    rem_proj_path = len(
        settings['projects_path'].replace('\\', '/').split('/'))
    proj_structure = path[rem_proj_path:]
    print(proj_structure)
    template_structure = settings['folder_structure']['asset'].replace(
        '\\', '/').split('/')
    print(template_structure)
    print(range(len(template_structure)))

    tokens = {}
    for i in range(len(template_structure)):

        token = template_structure[i]
        print(token)
        token_value = proj_structure[i]
        print(token_value)
        tokens.update({token: token_value})

    print(tokens)


if __name__ == '__main__':
    replace_tokens()
