import unittest
from src.kumites.kumite_math_analgeom import KumiteMathAnalGeom


class TestKumiteMathAnalGeom(unittest.TestCase):
    def test_binomial_expansion_1(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(x+1)^0"),"1","Yap")

    def test_binomial_expansion_2(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(x+1)^0"), "1","Yap")

    def test_binomial_expansion_3(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(x+1)^1"), "x+1","Yap")

    def test_binomial_expansion_4(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(x+1)^2"), "x^2+2x+1","Yap")

    def test_binomial_expansion_5(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(x-1)^0"), "1","Yap")

    def test_binomial_expansion_6(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(x-1)^1"), "x-1","Yap")

    def test_binomial_expansion_7(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(x-1)^2"), "x^2-2x+1","Yap")

    def test_binomial_expansion_8(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81","Yap")

    def test_binomial_expansion_9(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(2x-3)^3"), "8x^3-36x^2+54x-27","Yap")

    def test_binomial_expansion_10(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(7x-7)^0"), "1","Yap")

    def test_binomial_expansion_11(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81","Yap")

    def test_binomial_expansion_12(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(-2k-3)^3"), "-8k^3-36k^2-54k-27","Yap")

    def test_binomial_expansion_13(self):
        obj = KumiteMathAnalGeom()
        self.assertEqual(obj.binomial_expansion("(-7x-7)^0"), "1","Yap")
