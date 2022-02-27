import unittest

from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input(self):
        self.assertRaises(ValueError, lambda *_: french_to_english(None))

    def test_bonjour(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

class TestEnglishToFrench(unittest.TestCase):
    def test_null_input(self):
        self.assertRaises(ValueError, lambda *_: english_to_french(None))

    def test_hello(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")       

unittest.main()



