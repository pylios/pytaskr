## PyTaskr

PyTaskr is a lightweight task scheduler implemented in Python.  Scheduling tasks with it requires writing plugins for the system.  Plugins contain the schedule and operations for tasks, see the [helloworld](https://github.com/pylios/pytaskr/blob/main/src/plugins/helloworld) plugin for a simple example.  Plugins can specify their task schedule via crontab-like schedules (e.g. `5 15 * * *` would run at 3:05pm).

### Plugins
* Plugins can do essentially anything you could do in Python.  Parse files, lookup resources in AWS to check for compliance and make changes if needed, etc..
* Plugins are fairly easy to implement.  Neither advanced knowledge of Python nor the overall plugin and scheduling system is required.  If you can write Python, you can write a plugin.

## Docker
A Docker image is available for this plugin on [Dockerhub](https://hub.docker.com/repository/docker/pylios/pytaskr), if you would like to use it.  In order to run it locally with your own plugins, you should first create your plugins (see the [helloworld](https://github.com/pylios/pytaskr/blob/main/src/plugins/helloworld) example plugin) and place them in a plugins directory.  Then start the container with `docker run --rm -d --name pytaskr -v /path/to/your/plugins:/app/plugins pylios/pytaskr:latest` (replacing the first path with the path to the `plugins` folder you created).

Alternatively, a [Dockerfile](https://github.com/pylios/pytaskr/blob/main/src/Dockerfile) is provided in the repository, so that you can build your own image if desired.

### Crontab Reference
You might find [crontab guru](https://crontab.guru/) helpful in crafting crontab schedules for your tasks.

**Note**: crontab schedules are in UTC.


`* * * * *`

* 1st = minute
* 2nd = hour
* 3rd = day (month)
* 4th = month
* 5th = day (week)

#### Crontab Examples

* `5 15 * * *` At 15:05 (3:05pm)
* `5 15 5 * *` At 15:05 (3:05pm) on 5th day-of-month
* `5 15 * * 3` At 15:05 (3:05pm) on Wednesday

## Why on earth was this made
It was somewhat a learning effort on my part with Python.  But it's also handy to have a simple task scheduler that is portable between environments.