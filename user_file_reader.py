class UserFileReader():

    def __init__(self, file: str):
        self.__user_file = file
        self.__users = []

    def getUsers(self) -> list:
        return self.__users

    def read(self) -> None:
        with open(self.__user_file, 'r') as users:
            for user in [user.strip().strip("\n") for user in users.readlines()]:
                self.__users.append(user)
