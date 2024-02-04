from typing import Any, Optional


class InvalidServerKeyError(Exception):
    pass


class OutlineClients:
    __instance = None
    clients = {}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, server_name, outline_api_url):
        self._outline_api_url = self.__handle_server_key(outline_api_url)
        self.clients[server_name] = outline_api_url

    def __getattr__(self, server_name):
        if server_name in self.clients:
            return self.clients[server_name]
        else:
            print("Server not found")

    def set_server_url(self, server_name, outline_api_url):
        if server_name in self.clients:
            self.clients[server_name] = outline_api_url
        else:
            print("Server not found")

    def __del__(self):
        OutlineClients.__instance = None

    def __handle_server_key(self, outline_api_url: str) -> Optional[str]:
        """Adds unique keys, removes old ones if reassigned"""
        return outline_api_url


class OutlineServer:
    server_keys = set()

    def __init__(self, outline_api_url: str):
        self._outline_api_url = self.__handle_server_key(outline_api_url)

    def __handle_server_key(self, outline_api_url: str) -> Optional[str]:
        """Adds unique keys, removes old ones if reassigned"""

        if self.__validate_server_key(outline_api_url):
            try:
                self.__remove_server_key()
            finally:
                self.__add_server_key(outline_api_url)
                return outline_api_url

    def __validate_server_key(self, outline_api_url: str) -> bool:
        """Validates whether the server key is acceptable"""

        if self.__check_server_key(outline_api_url):
            raise InvalidServerKeyError(
                f"Key {outline_api_url} already exists")

        elif not isinstance(outline_api_url, str):
            raise InvalidServerKeyError("Key must be a string")

        elif len(outline_api_url.strip()) == 0:
            raise InvalidServerKeyError("Empty value")

        else:
            return True

    def __check_server_key(self, outline_api_url: str) -> bool:
        return outline_api_url in self.server_keys

    def __add_server_key(self, outline_api_url: str):
        self.server_keys.add(outline_api_url)

    def __remove_server_key(self):
        if self._outline_api_url in self.server_keys:
            self.server_keys.remove(self._outline_api_url)

    @property
    def server_key(self) -> Optional[str]:
        return self._outline_api_url

    @server_key.setter
    def server_key(self, outline_api_url: str):
        self._outline_api_url = self.__handle_server_key(
            outline_api_url)

    @server_key.deleter
    def server_key(self):
        del self._outline_api_url


# test = OutlineServer("123")
# test2 = OutlineServer("456")
