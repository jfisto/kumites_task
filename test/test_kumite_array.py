import unittest
import src.kumites.kumite_array as kumite


class TestKumiteFindArray(unittest.TestCase):
    # Testing function find_array
    def test_find_array_1(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array(['a', 'a', 'a', 'a', 'a'], [2, 4]), ['a', 'a'], "Yap")

    def test_find_array_2(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7]), [1, 1, 1], "Yap")

    def test_find_array_3(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array([1, 2, 3, 4, 5], [0]), [1], "Yap")

    def test_find_array_4(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array(['this', 'is', 'test'], [0, 1, 2]), ['this', 'is', 'test'], "Yap")

    def test_find_array_5(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array([0, 3, 4], [2, 6]), [4], "Yap")

    def test_find_array_6(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array([1], []), [], "Yap")

    def test_find_array_7(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array([], [2]), [], "Yap")

    def test_find_array_8(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array([], []), [], "Yap")

    def test_find_array_9(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.find_array([0, 3, 4, 7, 9, 11], [2, 6]), [4], "Yap")

    # Testing function solve()
    def test_solve_1(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("cozy"), 51)

    def test_solve_2(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("xyzzy"), 126)

    def test_solve_3(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("zodiac"), 26)

    def test_solve_4(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("chruschtschov"), 80)

    def test_solve_5(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("khrushchev"), 38)

    def test_solve_6(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("strength"), 57)

    def test_solve_7(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("twelfthstreet"), 103)

    def test_solve_8(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("catchphrase"), 73)

    def test_solve_9(self):
        obj = kumite.KumiteArray()
        self.assertEqual(obj.solve("mischtschenkoana"), 80)