#!/usr/bin/env python3
"""set_color_space_config.py
Description of set_color_space_config.py.
"""
from maya import cmds, mel


def main():
    """docstring for main"""
    var = 'ColorManagementConfigPathHistoryValue'
    # ocio = 'C:/Program Files/Autodesk/Maya2022/resources/OCIO-configs/Maya2022-default/config.ocio'
    ocio = '<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio'
    # ocio = 'C:/maya/config.ocio'

    # Replace line with color space config
    cmds.optionVar(sv=(var, ocio))
    mel.eval(f'changeColorMgtPrefsConfigFilePath("{ocio}")')
    path = cmds.optionVar(q=var)
    print(f'OCIO config path is {path}')


if __name__ == '__main__':
    main()
