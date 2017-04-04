import sys, pprint
from pysideuic import compileUi
pyfile = open("C:/Users/Sequence/Desktop/makeCube.py", 'w')
compileUi("C:/johannes/gdrive/scripts/sequence/maya/tools/exportNulls/ui/exportNulls.ui", pyfile, False, 4,False)
pyfile.close()