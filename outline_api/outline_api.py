from typing import Optional


class InvalidServerKeyError(TypeError):
    pass


class OutlineServer:
    server_keys = set()

    def __init__(self, outline_api_url: str):
        self._outline_api_url = self.__handle_server_key(
            outline_api_url, from_init=True)

    def __validate_server_key(self, outline_api_url: str) -> bool:
        if not isinstance(outline_api_url, str):
            print("Key must be a string")
            return False
        elif len(outline_api_url) == 0:
            print("Empty value")
            return False
        else:
            return True

    def __check_server_key(self, outline_api_url: str) -> bool:
        return outline_api_url in self.server_keys

    def __add_server_key(self, outline_api_url: str):
        self.server_keys.add(outline_api_url)

    def __remove_server_key(self):
        if self._outline_api_url in self.server_keys:
            self.server_keys.remove(self._outline_api_url)

    def __handle_server_key(self, outline_api_url: str,
                            from_init: bool = False) -> Optional[str]:

        if self.__check_server_key(outline_api_url):
            print(f"Key {outline_api_url} already exists!")
        elif self.__validate_server_key(outline_api_url):
            if from_init:
                print("CALL FROM INIT")
                self.__add_server_key(outline_api_url)
                return outline_api_url
            elif not from_init:
                print("CALL FROM SETTER")
                self.__remove_server_key()
                self.__add_server_key(outline_api_url)
                return outline_api_url
            else:
                raise InvalidServerKeyError("Invalid Outline API URL")

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
