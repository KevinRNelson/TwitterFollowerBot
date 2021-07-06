from twitter_application import NewFollowerApplicationBuilder
from twitter_bot import NewFollowerTwitterBotBuilder

from database import PickleDatabase
from notification import *
from user_file_reader import UserFileReader

EMAIL = 'keronels@ucsc.edu'
# FILE = 'users_test.txt'

#EMAIL = 'luckyguy1@gmail.com'
FILE = 'users.txt'

DATABASE = 'data.pkl'

CONSUMER_KEY        = 'eINzArE3PNaD0N7jHg21RvXsz'
CONSUMER_KEY_SECRET = 'cidYcrWYyz75sLkbrABsV9N2r2GhxZasNpWiDDh1jdPhulj8y6'

ACCESS_TOKEN        = '1368620185716809728-gCid7YMfvXlXYfH0niNpqmYPG22ats'
ACCESS_TOKEN_SECRET = 'xvQNBBnUa7VZlxBgQ44cbjt3eay8iIwwZ2UjihF92Bu62'

if __name__ == '__main__':
    bot = NewFollowerTwitterBotBuilder()                                       \
        .consumerKey(CONSUMER_KEY)                                             \
        .consumerKeySecret(CONSUMER_KEY_SECRET)                                \
        .accessToken(ACCESS_TOKEN)                                             \
        .accessTokenSecret(ACCESS_TOKEN_SECRET)                                \
        .waitOnRateLimit(True)                                                 \
        .build()

    application = NewFollowerApplicationBuilder()                              \
        .notificationObject(TimedNotification(Print(EMAIL)))                   \
        .databaseObject(PickleDatabase(DATABASE))                              \
        .fileReaderObject(UserFileReader(FILE))                                \
        .twitterBot(bot)                                                       \
        .build()

    application.setUp()
    application.run()
