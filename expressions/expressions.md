# Useful Maya Expressions

## Play every other frame of alembic
```
*remove the + 1 to do even frames*
if (frame % 2 == 0)
	example_AlembicNode.time = time + 1;
```


## Animate value to spin one full rotation over the duration of the animation
```
if (lightControl_CTRL.animateLights == true){
    lighting_GRP.rotateY = ((frame-defaultRenderGlobals.startFrame)/(defaultRenderGlobals.endFrame-defaultRenderGlobals.startFrame+1))*360;
} else {
	lighting_GRP.rotateY = 0;
}
```


## "Wiggle" expression
```
noise(time*2)*2;
```