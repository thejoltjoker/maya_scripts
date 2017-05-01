import Deadline.DeadlineConnect as Connect

if __name__ == '__main__':

    Deadline = Connect.DeadlineCon('supervisor-pc', 8082)

    JobInfo = {
        "Name": "Clayblast test submitted via Python",
        "Frames": "0-10",
        "Plugin": "MayaBatch",
        "Pool": "rnd",
        "Group": "redshift",
        "Comment": "Testing clayblasting",
        "Priority": "100"
        }

    PluginInfo = {
        "Version": "Max2014"
        }

    try:
        newJob = Deadline.Jobs.SubmitJob(JobInfo)
        print newJob
    except:
        print "Sorry, Web Service is currently down!"