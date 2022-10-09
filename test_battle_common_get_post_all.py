# Python代码中引入封装requests库的Common类
from common import Common

# 建立url_index的变量，存储战场的首页
url_index = '/'
# 实例化自己的Common
comm = Common()
# 调用你自己在Common封装的get方法，返回结果保存到response_index中
response_index = comm.get(url_index)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_index.text)

# uri_login存储战场的登录
url_login = '/login'
# username变量存储用户名参数
username = 'criss'
# password变量存储密码参数
password = 'criss'
# 拼凑body的参数
payload = 'username=' + username + '&password=' + password
# 实例化自己的Common
# comm = Common()
# 调用requests类的post方法，也就是HTTP的POST请求方式，
# 访问了url_login，其中通过将payload赋值给data完成body传参
response_login = comm.post(url_login, params=payload)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_login.text)

# uri_selectEq存储战场的选择武器
uri_selectEq = '/selectEq'
# 武器编号变量存储用户名参数
equipmentid = '10003'
# 拼凑body的参数
payload = 'equipmentid=' + equipmentid
# comm = Common()
response_selectEq = comm.post(uri_selectEq, params=payload)
print('Response内容：' + response_selectEq.text)

# uri_kill存储战场的选择武器
uri_kill = '/kill'
# 武器编号变量存储用户名参数
enemyid = '20001'
# 拼凑body的参数
payload = 'enemyid=' + enemyid + "&equipmentid=" + equipmentid
comm = Common()
response_kill = comm.post(uri_kill, params=payload)
print('Response内容：' + response_kill.text)
