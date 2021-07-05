import sys
sys.path.insert(0,'..')

from database import PickleDatabase
import unittest

EMPTY = 0
class TestDatabaseMethods(unittest.TestCase):

    def setUp(self):
        self.database = PickleDatabase('test.pkl')
        self.database.write({'keronels': ['lukaszkaiser']})
        self.database.read()

    def testRead(self):
        self.assertTrue(len(self.database.getFollowerMap()) != EMPTY)

    def testWrite(self):
        self.assertTrue(self.database.getFollowerMap()['keronels'][0] == 'lukaszkaiser')

    def testContainsAccount(self):
        self.assertTrue(self.database.containsAccount('keronels'))
        self.assertFalse(self.database.containsAccount('jabgarya'))

if __name__ == '__main__':
    unittest.main()
