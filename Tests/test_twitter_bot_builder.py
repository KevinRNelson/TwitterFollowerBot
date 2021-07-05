import sys
sys.path.insert(0,'..')

from twitter_bot import TwitterBot, TwitterBotBuilder
import unittest

CONSUMER_KEY        = 'eINzArE3PNaD0N7jHg21RvXsz'
CONSUMER_KEY_SECRET = 'cidYcrWYyz75sLkbrABsV9N2r2GhxZasNpWiDDh1jdPhulj8y6'

ACCESS_TOKEN   = '1368620185716809728-gCid7YMfvXlXYfH0niNpqmYPG22ats'
ACCESS_TOKEN_SECRET = 'xvQNBBnUa7VZlxBgQ44cbjt3eay8iIwwZ2UjihF92Bu62'

class TestTwitterBotBuilderMethods(unittest.TestCase):

    def setUp(self):
        self.bot = TwitterBotBuilder()              \
            .consumerKey(CONSUMER_KEY)              \
            .consumerKeySecret(CONSUMER_KEY_SECRET) \
            .accessToken(ACCESS_TOKEN)              \
            .accessTokenSecret(ACCESS_TOKEN_SECRET) \
            .waitOnRateLimit(True)

    def testConsumerKey(self):
        self.assertEqual(CONSUMER_KEY, self.bot.consumer_key)

    def testConsumerKeySecret(self):
        self.assertEqual(CONSUMER_KEY_SECRET, self.bot.consumer_key_secret)

    def testAccessToken(self):
        self.assertEqual(ACCESS_TOKEN, self.bot.access_token)

    def testAccessTokenSecret(self):
        self.assertEqual(ACCESS_TOKEN_SECRET, self.bot.access_token_secret)

    def testWaitOnRateLimit(self):
        self.assertEqual(True, self.bot.wait_on_rate_limit)

    def testBuild(self):
        self.assertTrue(isinstance(self.bot.build(), TwitterBot))

if __name__ == '__main__':
    unittest.main()
