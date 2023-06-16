import unittest
import src.kumites.kumite_array as kunite


class TestKumiteFindArray(unittest.TestCase):
    def test_find_array_1(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array(['a', 'a', 'a', 'a', 'a'], [2, 4]), ['a', 'a'], "Yap")

    def test_find_array_2(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7]), [1, 1, 1], "Yap")

    def test_find_array_3(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array([1, 2, 3, 4, 5], [0]), [1], "Yap")

    def test_find_array_4(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array(['this', 'is', 'test'], [0, 1, 2]), ['this', 'is', 'test'], "Yap")

    def test_find_array_5(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array([0, 3, 4], [2, 6]), [4], "Yap")

    def test_find_array_6(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array([1], []), [], "Yap")

    def test_find_array_7(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array([], [2]), [], "Yap")

    def test_find_array_8(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array([], []), [], "Yap")

    def test_find_array_9(self):
        obj = kunite.KumiteArray()
        self.assertEqual(obj.find_array([0, 3, 4, 7, 9, 11], [2, 6]), [4], "Yap")
