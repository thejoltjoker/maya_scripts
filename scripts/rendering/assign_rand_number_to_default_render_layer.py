"""
assign_rand_number_to_default_render_layer.py

Assigns a random number to defaultRenderLayer.
"""
import random
import maya.cmds as cmds


def main():
    all_nodes = cmds.ls(sl=True)
    for i in all_nodes:
        if ":defaultRenderLayer" in i:
            render_layer_name = i.replace("defaultRenderLayer",
                                          "renderLayerManager")
            rand_number = random.randint(0, 999)
            cmds.setAttr(render_layer_name + ".renderLayerId[0]", rand_number)


if __name__ == '__main__':
    main()