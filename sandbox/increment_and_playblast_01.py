import maya.cmds as cmds

# increment and save
cmds.file(force=True, save=True, options="v=0")

# get scene file name to name the playblast
pbFileName = cmds.file(q=True, sn=True, shn=True)

# render playblast
cmds.playblast(format="qt", filename="movies/"+pbFileName[:-3], clearCache=True, viewer=True,
               showOrnaments=False, fp=4, percent=100, compression="H.264", quality=75, widthHeight=[1280, 720])
