import Deadline.DeadlineConnect as Connect

if __name__ == '__main__':

    Deadline = Connect.DeadlineCon('supervisor-pc', 8082)

    scene_file_name_maya = "clayblast_Anm_Anm_Clay_v002.ma"
    scene_file_name = "clayblast_Anm_Anm_Clay_v002"
    scene_file_path = "P:/sequence_rnd_02/sequences/001/clayblast/Anm/work/maya"
    scene_file = '/'.join([scene_file_path, scene_file_name_maya])
    scene_file_output = '/'.join([scene_file_path, "images/"])
    scene_file_output_full = '/'.join([scene_file_path, "images/", scene_file_name])
    output_name = '.'.join([scene_file_name, "####.exr"])
    output_name_maya = '/'.join([scene_file_name, scene_file_name])
    min_time = '1'
    max_time = '10'
    frame_range = '-'.join([min_time, max_time])

    JobInfo = {
        "Frames": frame_range,
        "Group": "redshift",
        "Name": scene_file_name,
        "OutputDirectory0": scene_file_output_full,
        "OutputFilename0": output_name,
        "OverrideTaskExtraInfoNames": "False",
        "Plugin": "MayaBatch",
        "Pool": "rnd",

        }

    PluginInfo = {
        "Animation": "1",
        "FrameNumberOffset": "0",
        "GPUsPerTask": "0",
        "GPUsSelectDevices": "",
        "IgnoreError211": "0",
        "ImageHeight": "1080",
        "ImageWidth": "1920",
        "LocalRendering": "0",
        "OutputFilePath": scene_file_output,
        "OutputFilePrefix": output_name_maya,
        "ProjectPath": scene_file_path,
        "RedshiftVerbose": "2",
        "RenderHalfFrames": "0",
        "RenderLayer": "",
        "Renderer": "redshift",
        "SceneFile": scene_file,
        "StrictErrorChecking": "1",
        "UseLocalAssetCaching": "0",
        "UsingRenderLayers": "0",
        "Version": "2016.14",

        }

    try:
        newJob = Deadline.Jobs.SubmitJob(JobInfo, PluginInfo)
        print newJob
    except:
        print "Sorry, Web Service is currently down!"