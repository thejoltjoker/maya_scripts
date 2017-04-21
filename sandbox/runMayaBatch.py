def runbatch(file, script):    
    mayaBatchLocation = 'D:/software/Autodesk/Maya2016/bin/mayabatch'    
    command = '"%s" -prompt -batch -file "%s" -script "%s"' %(mayaBatchLocation, file, script)    
    os.system('"' + command + '"')    
runbatch(sys.argv[1], sys.argv[2])