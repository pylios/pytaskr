from yapsy.IPlugin import IPlugin
import time, datetime, os, ntpath


class PytaskrPlugin(IPlugin):
    meta = {}

    def __init__(self):
        self.parse_plugin_info()

    async def perform(self):
        raise NotImplementedError

    def plugin_info(self):
        return self.meta

    def get_schedule(self):
        return self.meta["crontab"]

    def parse_plugin_info(self):
        dir = os.path.dirname(os.path.realpath(__file__)) + "/../plugins"
        plugin_info_file = (
            dir
            + "/"
            + type(self).__name__.lower()
            + "/"
            + type(self).__name__.lower()
            + ".plugin"
        )
        f = open(plugin_info_file, "r")
        lines = f.read().splitlines()
        for line in lines:
            config = line.split("=")
            if len(config) > 1:
                self.meta[config[0].strip().lower()] = config[1].strip()
