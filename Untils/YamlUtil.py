# -*-coding: Utf-8 -*-
# @File : YamlUtil .py
# author:  Fengkui
# Time：2023/8/4
import os
import yaml


class YealReader:

    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None

    # 3、yaml读取
    # 单个文档读取
    def data(self):
        if not self._data:
            # 第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
            with open(self.yamlf, "rb") as f :
                self._data = yaml.safe_load_all(f)
            return self._data

    # 多个文档读取
    def data_all(self):
        #第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data_all:
            with open(self.yamlf, "rb") as f:
                self._data_all = yaml.safe_load_all(f)
            return self._data_all