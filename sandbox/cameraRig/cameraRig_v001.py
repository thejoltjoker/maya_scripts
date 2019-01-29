import maya.cmds as cmds

# create physical camera with two offset controls
camera -centerOfInterest 5 -focalLength 35 -lensSqueezeRatio 1 -cameraScale 1 -horizontalFilmAperture 1.41732 -horizontalFilmOffset 0 -verticalFilmAperture 0.94488 -verticalFilmOffset 0 -filmFit Fill -overscan 1 -motionBlur 0 -shutterAngle 144 -nearClipPlane 0.1 -farClipPlane 10000 -orthographic 0 -orthographicWidth 30 -panZoomEnabled 0 -horizontalPan 0 -verticalPan 0 -zoom 1; objectMoveCommand; cameraMakeNode 1 "";
curve -d 1 -p -1 1 1 -p 1 1 1 -p 1 -1 1 -p 1 -1 -1 -p 1 1 -1 -p -1 1 -1 -p -1 -1 -1 -p -1 -1 1 -p -1 1 1 -p -1 1 -1 -p -1 -1 -1 -p 1 -1 -1 -p 1 1 -1 -p 1 1 1 -p 1 -1 1 -p -1 -1 1 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 ;
# main control has camera settings f-stop, iso, shutter

# create object for focus pulling

# camera shake