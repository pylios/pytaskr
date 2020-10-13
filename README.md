# pytaskr

This is a lightweight task scheduler implemented in Python.  Scheduling tasks with it requires writing plugins for the system.  Plugins contain the schedule and operations for tasks, see the [helloworld](src/plugins/helloworld) plugin for a simple example.  Plugins can specify their task schedule via crontab-like schedules (e.g. `5 15 * * *` would run at 3:05pm).

## Creating Plugins

* Create a subdirectory under the `plugins` folder
* Your plugin filename and subdirectory name MUST match each other
* You MUST create a file with the same name but with the extension '.plugin' in the same directory as your plugin
    * e.g. if your plugin is helloworld/helloworld.py then you should also create helloworld/helloworld.plugin
    * An example of this file is located [here](src/plugins/helloworld/helloworld.plugin).
    * This file is where your Crontab schedule is held under the key `crontab`
* Crontab schedules are in UTC
* Plugins can do essentially anything you could do in Python.  Parse files, lookup resources in AWS to check for compliance and make changes if needed, etc..
* Plugins are fairly easy to implement.  Neither advanced knowledge of Python nor the overall plugin and scheduling system is required.  If you can write Python, you can write a plugin.

### Crontab Reference
You might find [crontab guru](https://crontab.guru/) helpful in crafting crontab schedules for your tasks.

**Note**: crontab schedules are in UTC.


`* * * * *`

* 1st = minute
* 2nd = hour
* 3rd = day (month)
* 4th = month
* 5th = day (week)

## Docker
This project can be easily containerized.  A `Dockerfile` is provided in the repository.  In order to build and use an image from it:

* Change into the `src` directory after cloning this repository
* Build the image by running `docker build --no-cache=true --rm -t pytaskr .`  
* Run the container with `docker run --rm -d --name pytaskr pytaskr`
* Output from the application can be viewed br running `docker logs -f pytaskr`

## Why on earth was this made
It was somewhat a learning effort on my part with Python.  But it's also handy to have a simple task scheduler that is portable between environments.
