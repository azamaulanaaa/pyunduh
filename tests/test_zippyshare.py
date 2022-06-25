import unittest
from pyunduh import zippyshare

class TestDefault(unittest.TestCase):
    def test_urlValidator(self):
        pairs = [
            (["https://raw.githubusercontent.com/azamaulanaaa/dotfiles/main/neovim/setup.sh"], False),
            (["https://www116.zippyshare.com/v/2WTfd7xd/file.html"], True),
        ]

        for pair in pairs:
            result = zippyshare.validateUrl(*pair[0])
            self.assertEqual(result, pair[1])

    def test_getServerCode(self):
        pairs = [
            (["https://www116.zippyshare.com/v/2WTfd7xd/file.html"], '116'),
        ]

        for pair in pairs:
            result = zippyshare.getServerCode(*pair[0])
            self.assertEqual(result, pair[1])

    def test_getFileCode(self):
        pairs = [
            (["https://www116.zippyshare.com/v/2WTfd7xd/file.html"], '2WTfd7xd'),
        ]

        for pair in pairs:
            result = zippyshare.getFileCode(*pair[0])
            self.assertEqual(result, pair[1])

    def test_Zippyshare(self):
        pairs = [
            (["https://www116.zippyshare.com/v/2WTfd7xd/file.html"], 'id,name,la'),
        ]
        
        for pair in pairs:
            res = zippyshare.Zippyshare(*pair[0])
            content = res.read(10).decode("utf-8")
            self.assertEqual(content, pair[1])



