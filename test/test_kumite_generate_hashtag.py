import unittest
import src.kumites.kumite_generate_hashtag as genhash

class TestKumiteGenerateHashtag(unittest.TestCase):
    def test_generate_hashtag_correct_1(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('Codewars'), '#Codewars', 'Should handle a single word.')

    def test_generate_hashtag_correct_2(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('Codewars      '), '#Codewars', 'Should handle trailing whitespace.')

    def test_generate_hashtag_correct_3(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('      Codewars'), '#Codewars', 'Should handle leading whitespace.')

    def test_generate_hashtag_correct_4(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('Codewars Is Nice'), '#CodewarsIsNice', 'Should remove spaces.')

    def test_generate_hashtag_correct_5(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('codewars is nice'), '#CodewarsIsNice',
                           'Should capitalize first letters of words.')

    def test_generate_hashtag_correct_6(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('CoDeWaRs is niCe'), '#CodewarsIsNice',
                           'Only the first letter of each word should be capitalized in the final hashtag, all other letters must be lower case.')

    def test_generate_hashtag_correct_7(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('c i n'), '#CIN',
                           'A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1.')

    def test_generate_hashtag_correct_8(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag('codewars  is  nice'), '#CodewarsIsNice',
                           'Should deal with unnecessary middle spaces.')

    def test_generate_hashtag_fixed_1(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag(''), False, 'Expected an empty string to return False')

    def test_generate_hashtag_fixed_2(self):
        obj = genhash.KumiteGenerate()
        self.assertEqual(obj.generate_hashtag(
            'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'),
                           False, 'Should return False if the final string is longer than 140 chars.')
