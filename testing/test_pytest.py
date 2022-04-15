# -*- coding: UTF-8 -*-
# Author:zxj
# date:2022-04-15
# -*- coding: UTF-8 -*-
# Author:zxj
# date:2022-04-15
import pytest

from python.caic import Calc
class TestCal:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        result = self.calc.add(1,2)
        print(result)
        assert 3 == result

    def test_div(self):
        result = self.calc.div(4,1)
        print(result)
        assert 2 == result
if __name__ == "__main__":
    pytest.main(['-vs','test_pytest.py::TestCal::test_div','test_pytest.py::TestCal::test_add_1'])
