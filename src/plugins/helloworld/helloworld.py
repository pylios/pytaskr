# Leave this line
from plugins.pytaskrplugin import PytaskrPlugin

# Import modules your plugin requires
import time, datetime

# You MUST inherit PytaskrPlugin
# You MUST choose a unique plugin name
class HelloWorld(PytaskrPlugin):
    meta = {}
    # You MUT implement a `perform` method
    async def perform(self):
        # Do whatever you want your plugin to do
        print("Someone is coming ...")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(15)
        print("Hello, world!")
        return True
