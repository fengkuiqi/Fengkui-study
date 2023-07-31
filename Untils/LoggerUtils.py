# -*-coding: Utf-8 -*-
# @File : LoggerUtils .py
# author:  Fengkui
# Time：2023/7/12
import datetime
import logging
import os
import time
from config.Conf import ConfigYaml

from config import Conf


class Logger:

    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(self.log_level)

        if not self.logger.handlers:
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(self.log_level)
            formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s ')
            fh_stream.setFormatter(formatter)

            fh_file = logging.FileHandler()
            fh_file.setLevel()
            fh_file.setLevel(formatter)

            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 1、初始化参数数据
# 日志文件名称，日志文件级别
# 日志文件名称 = logs目录 + 当前时间+扩展名
# log目录
log_path = Conf.get_logs_path()
# 当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
log_extension =".log"
logfile = os.path.join(log_path,current_time+log_extension)
# 日志文件级别
loglevel = "debug"
# 2、对外方法，初始log工具类，提供其它类使用

def my_log(log_name=__file__):
    return Logger(log_file=logfile, log_name=log_name, log_level=loglevel).logger

if __name__ == "__main__":
    my_log().debug("this is a debug")