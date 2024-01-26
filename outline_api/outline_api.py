import os
import requests


class OutlineServer:

    def __init__(self, outline_api_url):
        self.key = outline_api_url

    @property
    def key(self):
        return self.__outline_api_url

    @key.setter
    def key(self, outline_api_url):
        self.__outline_api_url = outline_api_url

    @key.deleter
    def key(self):
        del self.__outline_api_url


test = OutlineServer(os.getenv("VPN_API_URL"))
print(test.key)

test2 = OutlineServer(os.getenv("BOT_IP"))
print(test2.key)
