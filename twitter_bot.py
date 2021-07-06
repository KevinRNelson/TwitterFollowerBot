from abc import ABC, abstractmethod
import tweepy

class TwitterBotBuilder():

    def __init__(self):
        self.wait_on_rate_limit = True

    def consumerKey(self, consumer_key):
        self.consumer_key = consumer_key
        return self

    def consumerKeySecret(self, consumer_key_secret):
        self.consumer_key_secret = consumer_key_secret
        return self

    def accessToken(self, access_token):
        self.access_token = access_token
        return self

    def accessTokenSecret(self, access_token_secret):
        self.access_token_secret = access_token_secret
        return self

    def waitOnRateLimit(self, wait_on_rate_limit):
        self.wait_on_rate_limit = wait_on_rate_limit
        return self

    @abstractmethod
    def build(self):
        return TwitterBot(self)

class NewFollowerTwitterBotBuilder(TwitterBotBuilder):

    def __init__(self):
        super().__init__()

    def build(self):
        return NewFollowerTwitterBot(self)

class TwitterBot(ABC):

    @abstractmethod
    def __init__(self, builder: TwitterBotBuilder):
        pass

    @abstractmethod
    def setUp(self):
        pass

    @abstractmethod
    def run(self):
        pass

class NewFollowerTwitterBot(TwitterBot):

    def __init__(self, builder: NewFollowerTwitterBotBuilder):
        self.__consumer_key = builder.consumer_key
        self.__consumer_key_secret = builder.consumer_key_secret
        self.__access_token = builder.access_token
        self.__access_token_secret = builder.access_token_secret
        self.__wait_on_rate_limit = builder.wait_on_rate_limit

        self.__count = 200
        self.__accounts = []
        self.__follower_map = {}

    def getFollowerMap(self):
        return self.__follower_map

    def setUp(self, accounts: list, saved_follower_map: dict):
        self.__accounts = accounts
        self.__follower_map = dict(saved_follower_map)

        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_key_secret)
        auth.set_access_token(self.__access_token, self.__access_token_secret)

        self.api = tweepy.API(auth, wait_on_rate_limit=self.__wait_on_rate_limit)

    def run(self):
        try:
            self.getCurrentFollowers()
        except Exception as e:
            raise e

    def getCurrentFollowers(self):
        for account in self.__accounts:
            self.__follower_map[account] = []
            
            for follower in tweepy.Cursor(self.api.friends, account, count=self.__count).items():
                self.__follower_map[account].append(follower.screen_name)
