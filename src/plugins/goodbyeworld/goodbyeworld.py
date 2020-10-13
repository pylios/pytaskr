from support.pytaskrplugin import PytaskrPlugin

import time, datetime


class GoodbyeWorld(PytaskrPlugin):
    meta = {}

    async def perform(self):
        print("Someone is leaving ...")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(15)
        print("Goodbye, world!")
        return True
