import logging
import consts

"""
dfghj
"""
class OmdbBase:
    def __init__(self):
        self.url = consts.url + consts.api_key
        self.log = logging.getLogger()
        console = logging.StreamHandler()
        self.log.addHandler(console)
