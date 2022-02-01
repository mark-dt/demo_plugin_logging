This is a demo Extension for the Dynatrace OneAgent which has a helper function to restore correct logging functionality. It will create a specific logging folder for the extension in `/var/log/dynatrace/oneagent/plugin` and log into there. Built in automatic log rotation with up to 5 log files of max 1MB each of them.

```
azureuser@test log/dynatrace/oneagent/plugin
% pwd
/var/log/dynatrace/oneagent/plugin
azureuser@test log/dynatrace/oneagent/plugin
% l
total 88728
drwxr-xr-x 2 dtuser dtuser     4096 Feb  1 15:49 custom.python.demo_plugin_logging
-rw-r--r-- 1 dtuser dtuser    90268 Feb  1 16:01 oneagent_latest_snapshot.log

azureuser@test ~log/dynatrace/oneagent/plugin
% ll custom.python.demo_plugin_logging
total 12
-rw-r--r-- 1 dtuser dtuser 8256 Feb  1 15:57 demo_plugin_logging.log

```