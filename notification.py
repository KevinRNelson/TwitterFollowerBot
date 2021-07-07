from abc import ABC, abstractmethod
from message import *
import os

class Notification(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def notify(self, followed_accounts: dict, unfollowed_accounts: dict) -> None:
        pass


class CompositeNotification(Notification):

    def __init__(self):
        self.notifications = []

    def add(self, notification: Notification):
        self.notifications.append(notification)

    def notify(self, message: str) -> None:
        for notification in self.notifications:
            notification.notify(message)


from datetime import datetime
class TimedNotification(Notification):

    def __init__(self, notification: Notification):
        self.start_time = datetime.now().strftime('%x %X')
        self.notification = notification

    def notify(self, message: str) -> None:
        start_message = f"start time: {self.start_time}\n"

        self.end_time = datetime.now().strftime('%x %X')
        end_message   = f"end time:   {self.end_time}\n"

        message = start_message + end_message + "\n" + message
        self.notification.notify(message)


class PrintNotification(Notification):

    def __init__(self, out):
        self.out = out

    def notify(self, message: str) -> None:
        print(message)


class EmailNotification(Notification):

    def __init__(self, email: str):
        self.email = email

    def notify(self, message: str) -> None:
        os.system(f'echo "{message}" | mail -s "Twitter Bot - Updates" {self.email}')


class TestNotification(Notification):

    def __init__(self):
        self.notified = False

    def notify(self, message: str) -> None:
        self.notified = True
