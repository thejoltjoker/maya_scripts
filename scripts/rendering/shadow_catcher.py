#!/usr/bin/env python3
"""shadow_catcher.py
Create a shadow catcher under selected objects
"""


def create_shadow_catcher(self, target):
    """
        adds a floor under a given object
    """
    obj = cmds.exactWorldBoundingBox(target)

    size = 50 * (obj[4] - obj[1])
    floor = cmds.polyPlane(n=f'{target}_shadow_catcher', w=size, h=size)

    # place under the body
    floor_level = obj[1]
    cmds.move((obj[3] + obj[0]) / 2,  # bbox center
              floor_level,
              (obj[5] + obj[2]) / 2,  # bbox center
              floor, a=1)

    # Make the floor non-renderable
    shape = cmds.listRelatives(floor[0], shapes=True)
    cmds.setAttr(shape[0] + '.primaryVisibility', 0)

    return floor[0]


def main():
    """docstring for main"""
    pass


if __name__ == '__main__':
    main()
