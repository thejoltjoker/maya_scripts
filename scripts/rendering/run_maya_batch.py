#!/usr/bin/env python
"""
run_maya_batch.py
Description of run_maya_batch.py.
"""


def runbatch(file, script):
    """Run maya batch"""
    mayaBatchLocation = 'D:/software/Autodesk/Maya2016/bin/mayabatch'
    command = '"%s" -prompt -batch -file "%s" -script "%s"' % (
        mayaBatchLocation, file, script)
    os.system('"' + command + '"')


runbatch(sys.argv[1], sys.argv[2])