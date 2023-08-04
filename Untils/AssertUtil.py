# -*-coding: Utf-8 -*-
# @File : AssertUntils .py
# author:  Fengkui
# Time：2023/7/17
import json
from LoggerUtil import my_log


class AssertUtil:
    def __init__(self):
        self.log = my_log("AssertUtil")
    def assertcode(self, code, expected_code):
        try:
            if int(code) == int(expected_code):
                return True
        except:
            self.log.error("code error,code is %s,expected_code is %s" % (code, expected_code))

            raise

    def assertbody(self, body, expected_body):
        """
             验证返回结果内容相等
             :param body:
             :param expected_body:
             :return:
             """
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("body error,body is %s,expected_body is %s" % (body, expected_body))
            raise

    def assert_in_body(self, body, expected_body):
        """
        验证返回结果是否包含期望的结果
        :param body:
        :param expected_body:
        :return:
        """
        try:
            body = json.dumps(body)
            print(body)
            assert expected_body in body
            return True
        except:
            self.log.error("不包含或者body是错误，body is %s,expected_body is %s"%(body,expected_body))

            raise