# Python代码中引入封装requests库的Common类
from common import Common

# 首页的路由
uri = '/'
# 实例化自己的Common
comm = Common()
# 调用你自己在Common封装的get方法，返回结果保存到response_index中
response_index = comm.get(uri)
# 存储返回的response_index对象的text属性存储了访问主页的response信息，通过下面打印出来
print('Response内容：' + response_index.text)
