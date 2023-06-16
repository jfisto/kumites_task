import unittest
from src.kumites.kumite_cryptography import KumiteCryptography

class TestKumiteCryptography(unittest.TestCase):
    def test_keyword_cipher_1(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("Welcome home", "secret"), "wticljt dljt")

    def test_keyword_cipher_2(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("hello", "wednesday"), "bshhk")

    def test_keyword_cipher_3(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("HELLO", "wednesday"), "bshhk")

    def test_keyword_cipher_4(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("HeLlO", "wednesday"), "bshhk")

    def test_keyword_cipher_5(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("WELCOME HOME", "gridlocked"), "wlfimhl kmhl")

    def test_keyword_cipher_6(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("alpha bravo charlie", "delta"), "djofd eqdvn lfdqjga")

    def test_keyword_cipher_7(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("Home Base", "seven"), "dlja esqa")

    def test_keyword_cipher_8(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("basecamp", "covert"), "ocprvcil")

    def test_keyword_cipher_9(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("one two three", "rails"), "mks twm tdpss")

    def test_keyword_cipher_10(self):
        obj = KumiteCryptography()
        self.assertEqual(obj.keyword_cipher("Test", "unbuntu"), "raqr")
