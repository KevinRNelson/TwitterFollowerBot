from twitter_bot import TwitterBotBuilder
from database import PickleDatabase
from notification import *
from message import DefaultMessage
from change_in_followers import ChangeInFollowers
from user_file_reader import UserFileReader

EMAIL = 'keronels@ucsc.edu'
# FILE = 'users_test.txt'

#EMAIL = 'luckyguy1@gmail.com'
FILE = 'users.txt'

CONSUMER_KEY        = 'eINzArE3PNaD0N7jHg21RvXsz'
CONSUMER_KEY_SECRET = 'cidYcrWYyz75sLkbrABsV9N2r2GhxZasNpWiDDh1jdPhulj8y6'

ACCESS_TOKEN        = '1368620185716809728-gCid7YMfvXlXYfH0niNpqmYPG22ats'
ACCESS_TOKEN_SECRET = 'xvQNBBnUa7VZlxBgQ44cbjt3eay8iIwwZ2UjihF92Bu62'

if __name__ == '__main__':
    notification = TimedNotification(Print(EMAIL))

    file_reader = UserFileReader(FILE)
    file_reader.read()

    database = PickleDatabase()
    database.read()

    bot = TwitterBotBuilder()                                                  \
        .consumerKey(CONSUMER_KEY)                                             \
        .consumerKeySecret(CONSUMER_KEY_SECRET)                                \
        .accessToken(ACCESS_TOKEN)                                             \
        .accessTokenSecret(ACCESS_TOKEN_SECRET)                                \
        .waitOnRateLimit(True)                                                 \
        .setAccounts(file_reader.getUsers())                                   \
        .build()

    bot.setup()
    bot.run()

    followerMap = bot.getFollowerMap()
    database.write(followerMap)

    change_in_followers = ChangeInFollowers(database, followerMap)

    message = DefaultMessage(                                                  \
        change_in_followers.getFollowedAccounts(),                             \
        change_in_followers.getUnfollowedAccounts()                            \
    )
    message.format()
    notification.notify(message.getMessage())

    database.write(followerMap)
