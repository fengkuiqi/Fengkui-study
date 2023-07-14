# -*-coding: Utf-8 -*-
# @File : RequestsUntils .py
# author:  Fengkui
# Time：2023/7/12
import requests


def request_get(url, pars, headers):
    r = requests.get(url=url, params=pars, headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    res = dict()
    res["body"] = body
    res["code"] = code
    return res


def request_post(url, json=None, headers=None):
    r = requests.post(url=url, params=json, headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    res = dict()
    res["body"] = body
    res["code"] = code
    return res


class Requests:
    pass

    def request_api(self, url, data=None, json=None, headers=None, cookies=None, method=None):

        if method == "get":
            # get请求
            # self.log.debug("发送get请求")
            r = requests.get(url, data = data, json=json, headers=headers,cookies=cookies)
        elif method == "post":
            # post请求
            # self.log.debug("发送post请求")
            r = requests.post(url,data = data,  json=json, headers=headers,cookies=cookies)
        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        res = dict()
        res["body"] = body
        res["code"] = code
        return res

    def request_get(self, url, **kwargs):

        return self.request_api(url, method="get", **kwargs)

    def request_post(self, url, **kwargs):

        return self.request_api(url, method="post", **kwargs)