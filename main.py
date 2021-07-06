from twitter_application import NewFollowerApplicationBuilder
from twitter_bot import NewFollowerTwitterBotBuilder

from database import PickleDatabase
from notification import *
from file_reader import UserFileReader, ConfigFileReader

EMAIL = 'keronels@ucsc.edu'
# FILE = 'users_test.txt'

#EMAIL = 'luckyguy1@gmail.com'
FILE = 'users.txt'

DATABASE = 'data.pkl'
CONFIG_FILE = 'config.txt'

if __name__ == '__main__':
    application = NewFollowerApplicationBuilder()                              \
        .config_file(CONFIG_FILE)                                              \
        .notificationObject(TimedNotification(Print(EMAIL)))                   \
        .databaseObject(PickleDatabase(DATABASE))                              \
        .fileReaderObject(UserFileReader(FILE))                                \
        .build()

    application.setUp()
    application.run()
