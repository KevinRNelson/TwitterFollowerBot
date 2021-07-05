from abc import ABC, abstractmethod
import os

class Notification(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        pass


from datetime import datetime
class TimedNotification(Notification):

    def __init__(self, notification: Notification):
        self.start_time = datetime.now()
        self.notification = notification

    def notify(self, message: str) -> None:
        start_message = f"start time: {self.start_time}\n"

        self.end_time = datetime.now()
        end_message   = f"end time: {self.end_time}\n"

        message = start_message + end_message + message
        self.notification.notify(message)

class Print(Notification):

    def __init__(self, out):
        self.out = out

    def notify(self, message: str):
        print(message)


class Email(Notification):

    def __init__(self, email: str):
        self.email = email

    def notify(self, message: str) -> None:
        os.system(f'echo "{message}" | mail -s "Twitter Bot - Updates" {self.email}')
