for i in `ls -t *.*`; do
	if [[ "${i##*.}" != "exr" ]]; then
		echo 'Converting '$i
		/cygdrive/c/Program\ Files/Chaos\ Group/V-Ray/3dsmax\ 2016\ for\ x64/tools/img2tiledexr.exe $i ${i%.*}_tiled.exr
	fi
done