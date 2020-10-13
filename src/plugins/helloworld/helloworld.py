# You MUST import PytaskrPlugin
from support.pytaskrplugin import PytaskrPlugin

# You SHOULD import modules your plugin requires
import time, datetime

# You MUST inherit PytaskrPlugin
# You MUST choose a unique plugin name and it must match the filename
class HelloWorld(PytaskrPlugin):
    # You MUT declare this `meta` attribute
    meta = {}

    # You MUT implement a `perform` method
    async def perform(self):
        # Do whatever you want your plugin to do
        print("Someone is coming ...")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(15)
        print("Hello, world!")
        return True
