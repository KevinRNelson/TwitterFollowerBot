from twitter_application import NewFollowerApplicationBuilder
from notification import CompositeNotification, TimedNotification, EmailNotification, PrintNotification

KERONELS = 'keronels@ucsc.edu'
#USER_FILE = 'users_test.txt'

LUCKYGUY1 = 'luckyguy1@gmail.com'
USER_FILE = 'users.txt'

DATABASE = 'data.pkl'
CONFIG_FILE = 'config.txt'

if __name__ == '__main__':
    composite_notification = CompositeNotification()
    composite_notification.add(EmailNotification(KERONELS))
    composite_notification.add(EmailNotification(LUCKYGUY1))
    timed_notification = TimedNotification(composite_notification)

    application = NewFollowerApplicationBuilder()                              \
        .configFile(CONFIG_FILE)                                               \
        .userFile(USER_FILE)                                                   \
        .notificationObject(timed_notification)                                \
        .databaseFile(DATABASE)                                                \
        .build()

    application.setUp()
    application.run()
