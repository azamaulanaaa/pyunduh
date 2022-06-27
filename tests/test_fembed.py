import unittest
from pyunduh import fembed

class test_fembed(unittest.TestCase):
    def test_urlvalidator(self):
        pairs = [
            (["https://www.fembed.com/v/ny3rwa2n62y3-ww"], True),
            (["https://fembed.com/v/ny3rwa2n62y3-ww"], True),
            (["http://www.fembed.com/v/ny3rwa2n62y3-ww"], True),
            (["http://fembed.com/v/ny3rwa2n62y3-ww"], True),
            (["https://www116.zippyshare.com/v/2WTfd7xd/file.html"], False),
        ]

        for pair in pairs:
            result = fembed.validateUrl(*pair[0])
            self.assertEqual(result, pair[1])

    def test_getVideoId(self):
        pairs = [
            (["https://www.fembed.com/v/ny3rwa2n62y3-ww"], "ny3rwa2n62y3-ww"),
        ]

        for pair in pairs:
            result = fembed.getVideoId(*pair[0])
            self.assertEqual(result, pair[1])

    def test_Fembed(self):
        pairs = [
                (["https://fembed.com/v/ny3rwa2n62y3-ww"], "\x00\x00\x00 ftypis"),
        ]

        for pair in pairs:
            res = fembed.Fembed(*pair[0])
            content = res.read(10).decode("utf-8")
            self.assertEqual(content, pair[1])

