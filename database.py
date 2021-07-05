from abc import ABC, abstractmethod
import os

class Database(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getFollowerMap(self):
        pass

    @abstractmethod
    def getAccounts(self):
        pass

    @abstractmethod
    def getAccountFollowers(self, account):
        pass

    @abstractmethod
    def containsAccount(self, account):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


import pickle

class PickleDatabase(Database):

    def __init__(self, pickle_file='data.pkl'):
        self.__pickle_file = pickle_file
        self.__follower_map = {}

    def getFollowerMap(self) -> dict:
        return self.__follower_map

    def getAccounts(self) -> list:
        return self.__follower_map.keys()

    def getAccountFollowers(self, account: str) -> list:
        return self.__follower_map[account]

    def containsAccount(self, account: str) -> bool:
        return account in self.__follower_map.keys()

    def read(self) -> None:
        if self.__fileDoesNotExist():
            self.write(self.__follower_map)

        with open(self.__pickle_file, 'rb') as pickle_file:
            self.__follower_map = pickle.load(pickle_file)

    def __fileDoesNotExist(self) -> bool:
        return not os.path.isfile(self.__pickle_file)

    def write(self, data: dict) -> None:
        with open(self.__pickle_file, 'wb') as pickle_file:
            pickle.dump(data, pickle_file)
