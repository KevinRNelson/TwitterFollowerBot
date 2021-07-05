import sys
sys.path.insert(0,'..')

from message import DefaultMessage
import unittest

class TestMessageMethods(unittest.TestCase):

    def setUp(self):
        followed = {'keronels': ['jabgarya'], 'jabgarya': ['luckyguy1'], 'luckyguy1': []}
        unfollowed = {'keronels': ['luckyguy1'], 'luckyguy1': ['keronels'], 'jabgarya': ['keronels']}
        self.message = DefaultMessage(followed, unfollowed)

    def testFormat(self):
        self.message.format()
        self.assertEqual(2, self.message.getMessage().count('+'))
        self.assertEqual(3, self.message.getMessage().count('-'))

if __name__ == '__main__':
    unittest.main()
