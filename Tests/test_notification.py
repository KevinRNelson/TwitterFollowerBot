import sys
sys.path.insert(0,'..')

from notification import *
import unittest

class TestNotificationMethods(unittest.TestCase):

    # def setUp(self):


    def testTestNotification(self):
        notification = TestNotification()
        self.assertEqual(False, notification.notified)

    def testTestNotificationNotify(self):
        notification = TestNotification()
        notification.notify('hello world')
        self.assertEqual(True, notification.notified)

    def testTestCompositeNotification(self):
        composite_notification = CompositeNotification()
        composite_notification.add(TestNotification())
        composite_notification.add(TestNotification())
        composite_notification.notify('hello world')
        self.assertEqual(True, composite_notification.notifications[0].notified)
        self.assertEqual(True, composite_notification.notifications[1].notified)

    def testTestTimedCompositeNotification(self):
        notification1 = TestNotification()
        notification2 = TestNotification()

        composite_notification = CompositeNotification()
        composite_notification.add(notification1)
        composite_notification.add(notification2)

        timed_notification = TimedNotification(composite_notification)
        timed_notification.notify('hello world')

        self.assertEqual(True, notification1.notified)
        self.assertEqual(True, notification2.notified)

if __name__ == '__main__':
    unittest.main()
