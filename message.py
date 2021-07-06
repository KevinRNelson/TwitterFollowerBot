from abc import ABC, abstractmethod
import os

class Message():

    def __init__(self,
        recentlyFollowedAccounts: dict,
        recentlyUnfollowedAccounts: dict):

        self.accounts = list(set(recentlyFollowedAccounts.keys()) | set(recentlyUnfollowedAccounts.keys()))
        self.followed = recentlyFollowedAccounts
        self.unfollowed = recentlyUnfollowedAccounts
        self.message = ""

    def __format(self):
        pass


class NewFollowerDefaultMessage(Message):

    def __init__(self,
        recentlyFollowedAccounts: dict,
        recentlyUnfollowedAccounts: dict):

        super().__init__(recentlyFollowedAccounts, recentlyUnfollowedAccounts)

        self.__format()

    def __format(self):
        for account in self.accounts:
            if (self.__account_has_activity(account)):
                self.message += account + '\n'

                for followed_account in self.followed[account]:
                    self.message += "+" + followed_account + "\n"

                for unfollowed_account in self.unfollowed[account]:
                    self.message += "-" + unfollowed_account + "\n"

                self.message += "\n"

    def __account_has_activity(self, account: str) -> bool:
        return len(self.followed[account]) > 0 or len(self.unfollowed[account]) > 0

    def getMessage(self) -> str:
        return self.message
