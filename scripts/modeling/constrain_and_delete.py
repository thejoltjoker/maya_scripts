import maya.cmds as cmds
cmds.pointConstraint( w=1, mo=False );
cmds.orientConstraint( w=1, mo=False );
cmds.delete( cn=True );