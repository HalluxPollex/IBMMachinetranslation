
"""this is a docstring"""
#from email import message
#from msilib.schema import Error
#from types import NoneType
import unittest
import translator.translator


class TestFR(unittest.TestCase):
    """these are en to fr tests"""

    def test1(self):
        """this is hello test"""
        self.assertEqual(
            translator.translator.englishtofrench("Hello"), "Bonjour")

    def test2(self):
        """this is sentence test"""
        self.assertEqual(translator.translator.englishtofrench(
            "Hello, how are you?"), "Bonjour, comment es-tu?")

    def test3(self):
        """this is null input test, translator throws error whith None as input"""
        with self.assertRaises(Exception):
            translator.translator.englishtofrench(None)


class TestDE(unittest.TestCase):
    """these are en to de tests"""

    def test1(self):
        """this is hello test"""
        self.assertEqual(
            translator.translator.englishtogerman("Hello"), "Hallo")

    def test2(self):
        """this is sentence test"""
        self.assertEqual(translator.translator.englishtogerman("Hello, how are you?"),
                         "Hallo, wie geht es Ihnen?")

    def test3(self):
        """this is null input test, translator throws error whith None as input"""
        with self.assertRaises(Exception):
            translator.translator.englishtogerman(None)


unittest.main()
