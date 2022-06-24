import os

## The class has the following members:
# uuid: a device unique identifier (string)
# log_path: the file to write the process logs to

## This function is called on initialization
def setup(self):
    self.uuid = self.device.uuid
    self.log_path = os.path.join(CACHE_TRACES_DIRECTORY, self.log_name)

# Should restart the log capturing process (self.log_process)
# The capturing process will write the log content line by line to self.log_path
def start_log_trace_recording(self, level):
    #if it is already recording, kill the record as a previous instance failed to stop
    if self.log_capture:
        self.stop_log_trace_recoding(self)
    levels = {
        "verbose" : ["<Notice>","<Warning>","<Error>"],
        "info"    : ["<Notice>","<Warning>","<Error>"],
        "warning" : ["<Warning>","<Error>"],
        "error"   : ["<Error>"]
    }
    if os.path.exists(CACHE_TRACES_DIRECTORY):
        # Create the missing directory
        self.log.info("Create traces cache path: {}".format(CACHE_TRACES_DIRECTORY))
        os.mkdir(CACHE_TRACES_DIRECTORY)
    if os.path.exists(self.log_path):
        # Removing already existing file
        os.remove(self.log_path)
    try:
        self.log_file = open(self.log_path, "a")
        self.log_process = subprocess.Popen(["./devicelog", "-u", self.uuid], stdout=subprocess.PIPE, stderr=PIPE)
        if level and level in levels:
            callback = lambda line: self.read_line(line, levels[level])
        else:
            callback = lambda line: self.read_line(line, levels["verbose"])
        # redirect process output to self.log_path, apply callback on each line
        self.redirect_process_output(self.log_process, callback=callback)
    except Exception as e:
        self.log.error("Error creating trace log file for device {}. Error : {}".format(self.uuid, str(e)))
        return False
    self.log_capture = True
    return True

# This function returns a boolean describing if the process is stopped
# If the process is stopped, should return True, else should return False
def stop_log_trace_recording(self):
    if not self.is_process_running():
        return False
    self.log.info("Stopping device logging")
    if self.is_file_descriptor_open():
        self.log_file.close()

    self.log_process.wait()
    self.log_process = None
    self.log_capture = False
    self.set_process_running(False)
    return True