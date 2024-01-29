import os


class OutlineServer:
    server_keys = set()

    def __init__(self, outline_api_url):
        self.__outline_api_url = outline_api_url
        self.server_keys.add(outline_api_url)

    @classmethod
    def check_unique_key(cls, arg):
        return arg in cls.server_keys

    @property
    def key(self):
        return self.__outline_api_url

    @key.setter
    def key(self, outline_api_url):
        self.__outline_api_url = outline_api_url

    @key.deleter
    def key(self):
        self.server_keys.remove(self.__outline_api_url)
        del self.__outline_api_url


test = OutlineServer(123)
print(test.key)

test2 = OutlineServer(456)
print(test2.key)
