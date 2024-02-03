from typing import Optional


class InvalidServerKeyError(TypeError):
    pass


class OutlineServer:
    server_keys = set()

    def __init__(self, outline_api_url: str):
        self._outline_api_url = self.__handle_server_key(outline_api_url)

    def __handle_server_key(self, outline_api_url: str) -> Optional[str]:

        if self.__check_server_key(outline_api_url):
            raise InvalidServerKeyError(
                f"Key {outline_api_url} already exists")

        elif self.__validate_server_key(outline_api_url):
            try:
                self.__remove_server_key()
            finally:
                self.__add_server_key(outline_api_url)
                return outline_api_url

    def __validate_server_key(self, outline_api_url: str) -> bool:

        if not isinstance(outline_api_url, str):
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


test = OutlineServer("123")
test2 = OutlineServer("456")
