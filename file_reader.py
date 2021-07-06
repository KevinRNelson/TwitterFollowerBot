from abc import ABC, abstractmethod

class FileReader(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read(sef):
        pass


class UserFileReader(FileReader):

    def __init__(self, file: str):
        self.__user_file = file
        self.__users = []

    def getUsers(self) -> list:
        return self.__users

    def read(self) -> None:
        with open(self.__user_file, 'r') as users:
            for user in [user.strip().strip("\n") for user in users.readlines()]:
                self.__users.append(user)


class ConfigFileReader(FileReader):

    def __init__(self, file: str):
        self.__config_file = file
        self.__auth_keys = {
            'CONSUMER_KEY': '',
            'CONSUMER_KEY_SECRET': '',
            'ACCESS_TOKEN': '',
            'ACCESS_TOKEN_SECRET': '',
            'WAIT_ON_RATE_LIMIT': 'True'
        }

    def getAuthorization(self) -> dict:
        return self.__auth_keys

    def read(self) -> None:
        with open(self.__config_file, 'r') as config_file:
            for line in config_file.readlines():
                line = line.replace('\n', '')
                key = line.split(' ')[0]
                val = line.split(' ')[1]

                assert key in self.__auth_keys.keys()

                self.__auth_keys[key] = val

        # convert the value to a true boolean
        self.__auth_keys['WAIT_ON_RATE_LIMIT'] = self.__auth_keys['WAIT_ON_RATE_LIMIT'] == 'True'
