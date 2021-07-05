import tweepy

COUNT = 200

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

    def setAccounts(self, accounts: list):
        self.accounts = accounts
        return self

    def build(self):
        return TwitterBot(self)


class TwitterBot():

    def __init__(self, builder):
        self.__consumer_key = builder.consumer_key
        self.__consumer_key_secret = builder.consumer_key_secret
        self.__access_token = builder.access_token
        self.__access_token_secret = builder.access_token_secret
        self.wait_on_rate_limit = builder.wait_on_rate_limit
        self.accounts = builder.accounts

        self.__follower_map = {}

    def getFollowerMap(self):
        return self.__follower_map

    def setup(self):
        self.createApi()

    def createApi(self):
        self.api = tweepy.API(self.authentication(), wait_on_rate_limit=self.wait_on_rate_limit)

    def authentication(self):
        auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_key_secret)
        auth.set_access_token(self.__access_token, self.__access_token_secret)
        return auth

    def run(self):
        try:
            self.getCurrentFollowers()
        except Exception as e:
            raise e

    def getCurrentFollowers(self):
        for account in self.accounts:
            self.__follower_map[account] = []
            for follower in tweepy.Cursor(self.api.friends, account, count=COUNT).items():
                self.__follower_map[account].append(follower.screen_name)
