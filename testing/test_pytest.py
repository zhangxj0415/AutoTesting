# -*- coding: UTF-8 -*-
# Author:zxj
# date:2022-04-15
import pytest
import yaml, os
from python.demo import Calc


# 定义获取数据的类
class YamlData:
    def __init__(self, data_path):
        # 初始化数据获取yaml文件中数据
        self.data = yaml.safe_load(open(data_path))

    # 根据name获取想要的数据，norm或except
    def get_data(self, name):
        # 注意是字典
        return self.data[name]


# 获取到add和div数据
add_data = YamlData(os.path.join(os.path.dirname(os.path.dirname(__file__)), "datas", "add.yaml"))
div_data = YamlData(os.path.join(os.path.dirname(os.path.dirname(__file__)), "datas", "div.yaml"))


class TestCalc:
    # 获取要测试的方法
    def setup(self):
        self.calc = Calc()

    # 测试正常数据py
    @pytest.mark.parametrize('test_data', add_data.get_data('norm'))
    @pytest.mark.add  # 打标签
    def test_add_norm(self, test_data):
        result = self.calc.add(test_data['a'], test_data['b'])
        assert test_data['res'] == result

    # 测试异常数据
    @pytest.mark.parametrize('test_data', add_data.get_data('except'))
    @pytest.mark.xfail
    def test_add_except(self, test_data):
        result = self.calc.add(test_data['a'], test_data['b'])
        raise TypeError

    # 测试div正常数据
    @pytest.mark.parametrize('test_data', div_data.get_data('norm'))
    def test_div_norm(self, test_data):
        result = self.calc.div(test_data['a'], test_data['b'])
        assert test_data['res'] == result

    # 测试div异常数据
    @pytest.mark.parametrize('test_data', div_data.get_data('except'))
    @pytest.mark.xfail
    def test_div_except(self, test_data):
        result = self.calc.div(test_data['a'], test_data['b'])
        raise ZeroDivisionError


if __name__ == "__main__":
    # pytest.main(['-vs','test_pytest.py::TestCal::test_div','test_pytest.py::TestCal::test_add_1'])
    pytest.main(['-vs'])
