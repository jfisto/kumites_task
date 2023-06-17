import unittest
import src.kumites.kumite_array as kumit

class TestKumiteArraySolve(unittest.TestCase):
    def test_solve_1(self):
        obj = kumit.KumiteArray()
        self.assertEqual(obj.solve("cozy"), 51)

    def test_solve_exp(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve(1), 1)

    def test_solve_2(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("xyzzy"), 126)

    def test_solve_3(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("zodiac"), 26)

    def test_solve_4(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("chruschtschov"), 80)

    def test_solve_5(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("khrushchev"), 38)

    def test_solve_6(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("strength"), 57)

    def test_solve_7(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("twelfthstreet"), 103)

    def test_solve_8(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("catchphrase"), 73)

    def test_solve_9(self):
        obj = KumiteArray()
        self.assertEqual(obj.solve("mischtschenkoana"), 80)
