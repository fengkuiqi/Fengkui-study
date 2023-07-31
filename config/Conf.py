# -*-coding: Utf-8 -*-
# @File : Conf .py
# author:  Fengkui
# Time：2023/7/31
import os

# 获取当前文件绝对地址
current = os.path.abspath(__file__)

Base_DIR = os.path.dirname(os.path.dirname(current))

_log_path = Base_DIR + os.sep + "logs"


def get_logs_path():
   return _log_path


class ConfigYaml:
   pass