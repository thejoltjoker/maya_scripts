import maya.mel as mel

# Create beauty passes
mel.eval('rsCreateAov -type "Diffuse Filter"')
mel.eval('rsCreateAov -type "Diffuse Lighting Raw"')
mel.eval('rsCreateAov -type "Global Illumination Raw"')
mel.eval('rsCreateAov -type "Sub Surface Scatter"')
mel.eval('rsCreateAov -type "Specular Lighting"')
mel.eval('rsCreateAov -type "Reflections"')
mel.eval('rsCreateAov -type "Refractions"')
mel.eval('rsCreateAov -type "Emission"')
mel.eval('rsCreateAov -type "Caustics"')