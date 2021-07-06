class ChangeInFollowers():

    def __init__(self,
        saved_follower_map: dict,
        follower_map: dict
    ):

        accounts = follower_map.keys()

        self.__followed_accounts = {}
        self.__initializeFollowedAccountsDict(accounts)
        self.__followedAccounts(saved_follower_map, follower_map)

        self.__unfollowed_accounts = {}
        self.__initializeUnfollowedAccountsDict(accounts)
        self.__unfollowedAccounts(saved_follower_map, follower_map)

    def getFollowedAccounts(self):
        return self.__followed_accounts

    def getUnfollowedAccounts(self):
        return self.__unfollowed_accounts

    @staticmethod
    def __getDifference(followers1: list, followers2: list) -> list:
        return list(set(followers1) - set(followers2))

    def __followedAccounts(self, saved_follower_map: dict, follower_map: dict) -> None:
        accounts = follower_map.keys()

        for account in accounts:
            if account in saved_follower_map.keys():
                # obtains a list of followers that are followed that were not saved
                self.__followed_accounts[account] = ChangeInFollowers.__getDifference(follower_map[account], saved_follower_map[account])

    def __unfollowedAccounts(self, saved_follower_map: dict, follower_map: dict) -> None:
        accounts = saved_follower_map.keys()

        for account in accounts:
            if account in follower_map.keys():
                # obtains a list of follwers that were saved that are no longer followed
                self.__unfollowed_accounts[account] = ChangeInFollowers.__getDifference(saved_follower_map[account], follower_map[account])

    def __initializeFollowedAccountsDict(self, accounts: list) -> None:
        for account in accounts:
            self.__followed_accounts[account] = []

    def __initializeUnfollowedAccountsDict(self, accounts: list) -> None:
        for account in accounts:
            self.__unfollowed_accounts[account] = []
