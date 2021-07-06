from abc import ABC, abstractmethod

from twitter_bot import TwitterBotBuilder
from change_in_followers import ChangeInFollowers
from message import DefaultMessage

class ApplicationBuilder(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def twitterBot(self, bot):
        pass

    @abstractmethod
    def notificationObject(self, notification):
        pass

    @abstractmethod
    def databaseObject(self, database):
        pass

    @abstractmethod
    def fileReaderObject(self, file_reader):
        pass

    @abstractmethod
    def build(self):
        pass

class NewFollowerApplicationBuilder(ApplicationBuilder):

    def __init__(self):
        self.__bot = None
        self.__notification = None
        self.__database = None
        self.__file_reader = None

    def twitterBot(self, bot):
        self.bot = bot
        return self

    def notificationObject(self, notification):
        self.notification = notification
        return self

    def databaseObject(self, database):
        self.database = database
        return self

    def fileReaderObject(self, file_reader):
        self.file_reader = file_reader
        return self

    def build(self):
        return NewFollowerApplication(self)


class Application(ABC):

    @abstractmethod
    def setUp(self):
        pass

    @abstractmethod
    def run(self):
        pass

class NewFollowerApplication(Application):

    def __init__(self, builder: ApplicationBuilder):
        self.bot = builder.bot
        self.notification = builder.notification
        self.database = builder.database
        self.file_reader = builder.file_reader

    def setUp(self):
        self.database.read()

        self.file_reader.read()
        accounts = self.file_reader.getUsers()
        self.bot.setUp(accounts)


    def run(self):
        self.bot.run()

        followerMap = self.bot.getFollowerMap()
        self.database.write(followerMap)

        change_in_followers = ChangeInFollowers(self.database, followerMap)

        message = DefaultMessage(                                                  \
            change_in_followers.getFollowedAccounts(),                             \
            change_in_followers.getUnfollowedAccounts()                            \
        )
        self.notification.notify(message.getMessage())

        self.database.write(followerMap)
