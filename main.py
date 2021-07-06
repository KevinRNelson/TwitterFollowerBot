from twitter_application import NewFollowerApplicationBuilder
from notification import TimedNotification, Email, Print
from database import PickleDatabase

EMAIL = 'keronels@ucsc.edu'
#USER_FILE = 'users_test.txt'

#EMAIL = 'luckyguy1@gmail.com'
USER_FILE = 'users.txt'

DATABASE = 'data.pkl'
CONFIG_FILE = 'config.txt'

if __name__ == '__main__':
    application = NewFollowerApplicationBuilder()                              \
        .configFile(CONFIG_FILE)                                              \
        .userFile(USER_FILE)                                                   \
        .notificationObject(TimedNotification(Print(EMAIL)))                   \
        .databaseObject(PickleDatabase(DATABASE))                              \
        .build()

    application.setUp()
    application.run()
