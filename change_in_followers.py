from database import *

class ChangeInFollowers():

    def __init__(self,
        database: Database,
        follower_map: dict
    ):

        accounts = follower_map.keys()

        self.__followed_accounts = {}
        self.initializeFollowedAccountsDict(accounts)
        self.followedAccounts(database, follower_map)

        self.__unfollowed_accounts = {}
        self.initializeUnfollowedAccountsDict(accounts)
        self.unfollowedAccounts(database, follower_map)

    def getFollowedAccounts(self):
        return self.__followed_accounts

    def getUnfollowedAccounts(self):
        return self.__unfollowed_accounts

    @staticmethod
    def getDifference(followers1: list, followers2: list) -> list:
        return list(set(followers1) - set(followers2))

    def followedAccounts(self, database: Database, follower_map: dict) -> None:
        accounts = follower_map.keys()
        for account in accounts:
            if database.containsAccount(account):
                # obtains a list of followers that are followed that were not saved
                self.__followed_accounts[account] = self.getDifference(follower_map[account], database.getAccountFollowers(account))

    def unfollowedAccounts(self, database: Database, follower_map: dict) -> None:
        accounts = follower_map.keys()
        for account in database.getAccounts():
            if account in follower_map.keys():
                # obtains a list of follwers that were saved that are no longer followed
                self.__unfollowed_accounts[account] = self.getDifference(database.getAccountFollowers(account), follower_map[account])

    def initializeFollowedAccountsDict(self, accounts: list) -> None:
        for account in accounts:
            self.__followed_accounts[account] = []

    def initializeUnfollowedAccountsDict(self, accounts: list) -> None:
        for account in accounts:
            self.__unfollowed_accounts[account] = []
