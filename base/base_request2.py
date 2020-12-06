import requests
import json
import os

class BaseRequest(object):
    def send_get_request(self, url, data):
        res = requests.get(url=url, params=data)
        return res
    def send_post_requeat(self, url, data):
        res = requests.post(url=url, data=data)
        return res
    def run_rain(self, method, url, data):
        if method == 'get':
            res = self.send_get_request(url, data).text
        elif method == 'post':
            res = self.send_post_requeat(url, data).text
        else:
            print('请求方式不正确！')
        try:
            res = json.loads(res)
        except:
            print('这是一个text值！')
        return res


r = BaseRequest()