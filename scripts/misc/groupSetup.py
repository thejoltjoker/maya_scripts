import maya.cmds as cmds

# groups to be created
groupList = ['geo_grp', 'light_grp', 'cam_grp', 'sim_grp']

cmds.group( em=True, name='scene_grp' )

# create groups
for g in groupList:
	cmds.group( em=True, name=g )
	cmds.parent( g, 'scene_grp')

groupList.append('scene_grp')

# lock group attributes
for l in groupList:
	cmds.setAttr( l + '.translateX', lock=True )
	cmds.setAttr( l + '.translateY', lock=True )
	cmds.setAttr( l + '.translateZ', lock=True )
	cmds.setAttr( l + '.scaleX', lock=True )
	cmds.setAttr( l + '.scaleY', lock=True )
	cmds.setAttr( l + '.scaleZ', lock=True )
	cmds.setAttr( l + '.rotateX', lock=True )
	cmds.setAttr( l + '.rotateY', lock=True )
	cmds.setAttr( l + '.rotateZ', lock=True )