import maya.cmds as cmds
import datetime
 
i = datetime.datetime.now() 
currentTime = i.strftime('%Y-%m-%d')

# increment and save
# cmds.file(force=True, save=True, options="v=0");

# get scene file name to name the playblast
pbFileName = cmds.file(q=True, sn=True, shn=True);

# set bg color
cmds.displayRGBColor( 'background', 0, 1, 0 )

# render playblast
cmds.playblast(format="qt", filename="movies/"+currentTime+"/"+pbFileName[:-3], clearCache=True, viewer=True, showOrnaments=False, fp=4, percent=100, compression="H.264", quality=75, widthHeight=[1280, 720]);

# set bg color back
cmds.displayRGBColor( 'background', rs=True )