@ECHO OFF
COLOR 02
ECHO Processing %~1
"C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe" "%~dp0\fix_color_space_standalone.py" "%~1"
ECHO Finished!
pause