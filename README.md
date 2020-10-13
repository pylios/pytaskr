# pytaskr

This is a lightweight task scheduler implemented in Python.  Scheduling tasks with it requires writing plugins for the system.  Plugins contain the schedule and operations for tasks, see the [helloworld](src/plugins/helloworld) plugin for a simple example.  Plugins can specify their task schedule via crontab-like schedules (e.g. `5 15 * * *` would run at 3:05pm).

## Creating Plugins

* Create a subdirectory under the `plugins` folder
* Your plugin filename and subdirectory name MUST match each other
* You MUST create a file with the same name but with the extension '.plugin' in the same directory as your plugin
    * e.g. if your plugin is helloworld/helloworld.py then you should also create helloworld/helloworld.plugin
    * An example of this file is located [here](src/plugins/helloworld/helloworld.plugin).
    * This file is where your Crontab schedule is held under the key `interval`
* Crontab schedules are in UTC

## Crontab Reference
`* * * * *`

* 0 = minute
* 1 = hour
* 2 = day (month)
* 3 = month
* 4 = day (week)

### Crontab Examples

* `5 15 * * *` At 15:05
* `5 15 5 * *` At 15:05 on day-of-month 5
* `5 15 * * 3` At 15:05 on Wednesday

## Docker
This project can be easily containerized.  A `Dockerfile` is provided in the repository.  In order to build and use an image from it:

* Change into the `src` directory after cloning this repository
* Build the image by running `docker build --no-cache=true --rm -t pytaskr .`  
* Run the container with `docker run --rm -d --name pytaskr pytaskr`
* Output from the application can be viewed br running `docker logs -f pytaskr`