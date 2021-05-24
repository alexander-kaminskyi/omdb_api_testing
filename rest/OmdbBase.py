import logging
import consts


class OmdbBase:
    def __init__(self):
        self.url = consts.url + consts.api_key
        self.log = logging.getLogger()
        console = logging.StreamHandler()
        self.log.addHandler(console)
