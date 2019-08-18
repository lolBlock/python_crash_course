# coding = utf-8

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """TestCase中包含了方法setUp,若重写了，python将在运行test前运行setUp，可以使用其中创建的对象"""
        question = "你有哪几个舍友？"
        self.survey = AnonymousSurvey(question)  # 创建一个调查对象
        self.responses = ['wu guangqiang', 'hu xuefeng', 'cheng chao']

    def test_store_one_response(self):
        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)

    def test_store_tree_responses(self):
        for response in self.responses:
            self.survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)
