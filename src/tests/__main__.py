import unittest
from sys import modules
from os.path import abspath, dirname

def getPWD():
    filepath = modules["__main__"].__file__
    if filepath == None:
        return None
    dirpath = abspath(dirname(filepath))
    return dirpath

if __name__ == "__main__":
    pwd = getPWD()
    if pwd == None:
        exit()
    suite = unittest.TestLoader().discover(pwd)
    unittest.TextTestRunner().run(suite)
