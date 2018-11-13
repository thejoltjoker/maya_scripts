import maya.standalone
import maya.cmds as cmds
maya.standalone.initialize(name='python')


print(cmds.polyCube())
