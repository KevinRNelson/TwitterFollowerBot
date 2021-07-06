import sys
sys.path.insert(0, '..')

from file_reader import ConfigFileReader
import unittest

EMPTY = 0
class TestChangeInFollowersMethods(unittest.TestCase):

    def setUp(self):
        self.config_file_reader = ConfigFileReader('config_test.txt')
        self.config_file_reader.read()

    def testConsumerKey(self):
        self.assertEqual('jwhrbf786234t3uihgfb3908g', self.config_file_reader.getAuthorization()['CONSUMER_KEY'])

    def testConsumerKeySecret(self):
        self.assertEqual('kjrbg80375g8o34gbn804vh4398uvb4vgb49pv', self.config_file_reader.getAuthorization()['CONSUMER_KEY_SECRET'])

    def testAccessToken(self):
        self.assertEqual('2112474246524582956-wdkvjhb3807g38ipvb387gv3934b4', self.config_file_reader.getAuthorization()['ACCESS_TOKEN'])

    def testAccessTokenSecret(self):
        self.assertEqual('3unrgb983h93b4n84gve8vbekgj49855t673', self.config_file_reader.getAuthorization()['ACCESS_TOKEN_SECRET'])

    def testWaitOnRateLimit(self):
        self.assertEqual(False, self.config_file_reader.getAuthorization()['WAIT_ON_RATE_LIMIT'])

if __name__ == '__main__':
    unittest.main()
