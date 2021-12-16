import maya.cmds as cmds


def sample_updater(sample_count):
    lights = cmds.ls(type=['light', 'RedshiftPhysicalLight'])

    for light in lights:
        if cmds.getAttr(light + ".volumeRayContributionScale") > 0:
            cmds.setAttr(light + ".volumeNumSamples", sample_count)
            print(light)


# WORKS
# lights = cmds.ls(type=['light', 'RedshiftPhysicalLight'])

# sample_count = 512

# for light in lights:
#     if cmds.getAttr(light+".volumeRayContributionScale") > 0:
#         cmds.setAttr(light+".volumeNumSamples", sample_count)
#         print light


cmds.window()

cmds.columnLayout()

cmds.rowColumnLayout(numberOfColumns=1)
cmds.intSliderGrp(field=True, label='Samples',
                  min=4, max=4096, step=4,
                  columnWidth3=[50, 50, 100],
                  columnAlign3=['left', 'left', 'left'],
                  adjustableColumn3=3)
cmds.rowColumnLayout(numberOfColumns=2,
                     columnSpacing=[(2, 77)],
                     columnWidth=[(2, 100)])
cmds.text(label='Users')
cmds.intSlider()

cmds.showWindow()
