# Internal

What bugs did we add in this code example ?

## Bad condition

```
if os.path.exists(CACHE_TRACES_DIRECTORY):
        # Create the missing directory
        self.log.info("Create traces cache path: {}".format(CACHE_TRACES_DIRECTORY))
        os.mkdir(CACHE_TRACES_DIRECTORY)
```

Should be `if not os.path.exists` instead of `if os.path.exists`

## Missing import

Missing subprocess import
`import subprocess` at the top of the file

## Missing package specifier

`stderr=PIPE` should be `stderr=subprocess.PIPE` like stdout.

## Missing kill

In `stop_log_trace_recording` there is a missing call to `self.log_process.kill()`