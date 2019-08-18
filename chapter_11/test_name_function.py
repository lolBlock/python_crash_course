# coding = utf-8
# 自动测试get_formatted_name
"""测试函数"""

import unittest
from name_function import get_formatted_name


class NameTestCase(unittest. TestCase):  # 必须要继承TestCase
    """测试get_formatted_name"""

    def test_first_last_name(self):  # 方法名必须以test开头
        """是否可以正确处理cheng chao这类名字"""
        format_name = get_formatted_name('chao', 'cheng')
        self.assertEqual(format_name, 'Chao Cheng')

    def test_first_middle_last_name(self):
        """是否可以正确处理wU GUANGqiang这类名字"""
        format_name = get_formatted_name('guAngqiang', 'wU')
        self.assertEqual(format_name, 'Guangqiang Wu')


if __name__ == '__main__':
    unittest.main()  # 新版本的pip不能只使用这一句，还要加上一句
