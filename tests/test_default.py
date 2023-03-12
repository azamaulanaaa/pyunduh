import unittest
from pyunduh import default

class test_default(unittest.TestCase):
    def test_Default(self):
        pairs = [
            (["https://github.com/azamaulanaaa/pyunduh/raw/master/setup.py"], 'import set'),
        ]

        for pair in pairs:
            res = default.Default(*pair[0])
            content = res.read(10).decode("utf-8")
            self.assertEqual(content, pair[1])
