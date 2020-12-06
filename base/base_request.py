import requests
import json


class BaseRequesrt(object):

    def send_get_request(self, url, data):
        '''

        :param url:
        :param data:
        :return: 发送get请求，返回的是text
        '''
        res = requests.get(url=url, params=data).text
        return res

    def send_post_request(self, url, data):
        '''
        发送get请求，返回的是text
        :param url:
        :param data:
        :return:
        '''
        res = requests.post(url=url, data=data).text
        return res

    def run_main(self, method, url, data):
        '''
        指定请求方式，请求地址，data
        格式已转化为一个json格式进行返回，如果返回不了，就是一个text值
        :param method:
        :param url:
        :param data:
        :return:
        '''
        if method == 'get':
            res = self.send_get_request(url, data)
        elif method == 'post':
            res = self.send_post_request(url, data)
        else:
            print('请求方式传参不正确！')
        try:
            res = json.loads(res)
        except:
            print('这个结果是一个text值！')
        return res


request = BaseRequesrt()
