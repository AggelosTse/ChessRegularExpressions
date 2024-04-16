import unittest
from my_re_functions import (chessmatch,finddate,findelodifference,findmovesum,findwinner)


class TestTriangles(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(findwinner(chessmatch), "Draw")
        self.assertAlmostEqual(findelodifference(chessmatch), 7)
        self.assertAlmostEqual(finddate(chessmatch), "09.04.2023")
        self.assertAlmostEqual(findmovesum(chessmatch), 49)


if __name__ == "__main__":
    unittest.main()
