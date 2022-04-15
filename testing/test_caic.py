# -*- coding: UTF-8 -*-
# Author:zxj
# date:2022-04-15
import unittest
import sys
sys.path.append('..')
from python.caic import Calc

class TestCal(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1,2)
        print(result)
        self.assertEqual(3,result)

if __name__ == '__main__':
    unittest.main()