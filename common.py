import requests


# 定义一个common类，它的父类是object
class Common(object):
    # common类的构造函数
    def __init__(self):
        # 被测系统的根路由
        self.url_root = 'http://127.0.0.1:12356'

    # 封装你自己的get请求，uri是访问路由，params是get请求的参数，如果没有默认为空
    def get(self, uri, params=''):
        # 拼凑访问地址
        url = self.url_root + uri + params
        # 通过get请求访问对应地址
        res = requests.get(url)
        # 返回request的response结果，类型为requests的response类型
        return res

    # 封装你自己的post请求，uri是访问路由，params是post请求襖传递的参数，如果没有参数这里为空
    def post(self, uri, params=''):
        # 拼凑访问地址
        url = self.url_root + uri
        if len(params) > 0:
            # 如果有参数，那么通过post方式访问对应url，并将参数赋值给requests.post默认参数data
            res = requests.post(url, data=params)
        else:
            # 如果无参数，访问方式如下
            # 返回request的response结果，类型为requests的response类型
            res = requests.post(url, data=params)
        return res
