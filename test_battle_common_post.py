# Python代码中引入封装requests库的Common类
from common import Common

# 登录页路由
uri = '/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
# 实例化自己的Common
comm = Common()
# 访问了url_login，其中通过将payload赋值给data完成body传参
response_login = comm.post(uri, params=payload)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_login.text)
