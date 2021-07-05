import sys
sys.path.insert(0,'..')

from user_file_reader import UserFileReader
import unittest

class TestUserFileReaderMethods(unittest.TestCase):

    def setUp(self):
        self.user_file_reader = UserFileReader('users.txt')
        self.user_file_reader.read()

    def testRead(self):
        self.assertTrue('keronels' in self.user_file_reader.users())
        self.assertTrue('lukaszkaiser' in self.user_file_reader.users())

if __name__ == '__main__':
    unittest.main()
