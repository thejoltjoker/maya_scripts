import maya.cmds as cmds
import random
all_nodes = cmds.ls(sl=True)
for i in all_nodes:
    if ":defaultRenderLayer" in i:
        render_layer_name = i.replace("defaultRenderLayer","renderLayerManager")
        rand_number = random.randint(0,999)
        cmds.setAttr(render_layer_name+".renderLayerId[0]", rand_number)