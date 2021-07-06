from abc import ABC, abstractmethod

from twitter_bot import TwitterBotBuilder
from file_reader import UserFileReader
from change_in_followers import ChangeInFollowers
from message import DefaultMessage

class ApplicationBuilder(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def configFile(self):
        pass

    @abstractmethod
    def userFile(self, user_file):
        pass

    @abstractmethod
    def notificationObject(self, notification):
        pass

    @abstractmethod
    def databaseObject(self, database):
        pass

    @abstractmethod
    def build(self):
        pass

class NewFollowerApplicationBuilder(ApplicationBuilder):

    def __init__(self):
        self.config_file = None
        self.notification = None
        self.database = None
        self.file_reader = None

    def configfile(self):
        self.config_file = config_file
        return self

    def userFile(self, user_file):
        self.user_file = user_file
        return self

    def notificationObject(self, notification):
        self.notification = notification
        return self

    def databaseObject(self, database):
        self.database = database
        return self

    def build(self):
        return NewFollowerApplication(self)


class Application(ABC):

    @abstractmethod
    def __createBot(self, config_file: str) -> TwitterBot:
        pass

    @abstractmethod
    def setUp(self):
        pass

    @abstractmethod
    def run(self):
        pass

class NewFollowerApplication(Application):

    def __init__(self, builder: ApplicationBuilder):
        self.bot = self.__createBot(builder.config_file)
        self.file_reader = UserFileReader(builder.file_reader)
        self.notification = builder.notification
        self.database = builder.database

    def __createBot(self, config_file: str) -> NewFollowerTwitterBot:
        config_file_reader = ConfigFileReader(config_file)
        config_file_reader.read()

        authorization = config_file_reader.getAuthorization()
        return NewFollowerTwitterBotBuilder()                                  \
            .consumerKey(authorization['CONSUMER_KEY'])                        \
            .consumerKeySecret(authorization['CONSUMER_KEY_SECRET'])           \
            .accessToken(authorization['ACCESS_TOKEN'])                        \
            .accessTokenSecret(authorization['ACCESS_TOKEN_SECRET'])           \
            .waitOnRateLimit(authorization['WAIT_ON_RATE_LIMIT'])              \
            .build()

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

        message = DefaultMessage(                                              \
            change_in_followers.getFollowedAccounts(),                         \
            change_in_followers.getUnfollowedAccounts()                        \
        )
        self.notification.notify(message.getMessage())

        self.database.write(followerMap)
