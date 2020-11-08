from support.pytaskrplugin import PytaskrPlugin

import time, datetime


class GoodbyeWorld(PytaskrPlugin):
    meta = {}

    async def perform(self):
        print("Someone is leaving ...")
        time.sleep(15)
        print("Goodbye, world!")
        return True
