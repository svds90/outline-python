import os


class OutlineServer:

    def __init__(self, outline_api_url):
        self._outline_api_url = outline_api_url

    @property
    def server_key(self):
        return self._outline_api_url

    @server_key.setter
    def server_key(self, outline_api_url):
        self._outline_api_url = outline_api_url

    @server_key.deleter
    def server_key(self):
        del self._outline_api_url


test = OutlineServer(123)
test2 = OutlineServer(456)
