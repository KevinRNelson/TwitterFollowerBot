import sys
sys.path.insert(0,'..')

from database import PickleDatabase
from change_in_followers import ChangeInFollowers
import unittest

EMPTY = 0
class TestChangeInFollowersMethods(unittest.TestCase):

    def setUp(self):
        self.database = PickleDatabase('test.pkl')
        self.database.write({'keronels': ['lukaszkaiser']})
        self.database.read()

        self.changeInFollowers = ChangeInFollowers(self.database.getFollowerMap(), {'keronels': ['jabgarya']})

    def testGetRecentlyFollowedAccounts(self):
        self.assertEqual({'keronels': ['jabgarya']}, self.changeInFollowers.getFollowedAccounts())

    def testGetRecentlyUnfollowedAccounts(self):
        self.assertEqual({'keronels': ['lukaszkaiser']}, self.changeInFollowers.getUnfollowedAccounts())

if __name__ == '__main__':
    unittest.main()
