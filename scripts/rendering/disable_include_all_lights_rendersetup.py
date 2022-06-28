#!/usr/bin/env python3
"""disable_include_all_lights_rendersetup.py
Disable the worst feature of them all.
"""


def main():
    """docstring for main"""
    cmds.optionVar(iv=('renderSetup_includeAllLights', 0))

    # optionVar -iv "renderSetup_includeAllLights" 0


if __name__ == '__main__':
    main()
