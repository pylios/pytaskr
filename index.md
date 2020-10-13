## PyTaskr

PyTaskr is a lightweight task scheduler implemented in Python.  Scheduling tasks with it requires writing plugins for the system.  Plugins contain the schedule and operations for tasks, see the [helloworld](src/plugins/helloworld) plugin for a simple example.  Plugins can specify their task schedule via crontab-like schedules (e.g. `5 15 * * *` would run at 3:05pm).

### Plugins
* Plugins can do essentially anything you could do in Python.  Make a web request on a predefined schedule, lookup resources in AWS to check for compliance and make changes if needed, etc..
* Plugins are fairly easy to implement.  Advanced knowledge of Pythonor the overall plugin and scheduling system isn't required.  If you can write Python, you can write a plugin.

## Docker
This project can be easily containerized.  A `Dockerfile` is provided in the repository.  While an image is made available on [Dockerhub](https://hub.docker.com/repository/docker/pylios/pytaskr), it would probably be best for you to build your own image using [instructions in the ReadMe](https://github.com/pylios/pytaskr#docker) so you can more easily include your own plugins<sup><a href="foot-1">1</a></sup>

### Crontab Reference
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

<a id="foot-1"></a>1. Planning to add in support for mounting a volume with your own plugins in the future; I just haven't gotten around to it yet.