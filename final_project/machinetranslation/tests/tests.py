import unittest
from translator import english_to_french,french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertEqual(english_to_french(''), 'The text is empty, Please input some text to translate')


class TestFrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertEqual(french_to_english(''), 'The text is empty, Please input some text to translate')

unittest.main()
