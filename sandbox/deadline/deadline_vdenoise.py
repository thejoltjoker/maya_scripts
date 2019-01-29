import re
from System.IO import *
from Deadline.Scripting import *


def __main__(*args):
    deadlinePlugin = args[0]
    job = deadlinePlugin.GetJob()
    outputDirectories = job.OutputDirectories
    outputFilenames = job.OutputFileNames
    paddingRegex = re.compile("[^\\?#]*([\\?#]+).*")

    for i in range(0, len(outputDirectories)):
        outputDirectory = outputDirectories[i]
        outputFilename = outputFilenames[i]

        startFrame = deadlinePlugin.GetStartFrame()
        endFrame = deadlinePlugin.GetEndFrame()
        for frameNum in range(startFrame, endFrame + 1):
            outputPath = Path.Combine(outputDirectory, outputFilename)
            outputPath = outputPath.replace("//", "/")

            m = re.match(paddingRegex, outputPath)
            if(m != None):
                padding = m.group(1)
                frame = StringUtils.ToZeroPaddedString(
                    frameNum, len(padding), False)
                outputPath = outputPath.replace(padding, frame)

            deadlinePlugin.LogInfo("Output file: " + outputPath)
