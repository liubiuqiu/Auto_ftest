"""
目标：实现登陆接口封装
"""
#导入 requests 包
import requests

#新建类 登录接口对象
class Apilogin():
    # 新建方法 登录方法
        def api_login(self,url,mobile,code):
        # headers 定义
        headers = {"Conent-Type": "value"}
        # data 定义
        data ={"mobile":mobile,"code":code}
        # 调用post 返回响应对象
        return requests.post(url,headers =headers, json= data)

"""
提示：url ，mobile，code 都需要从data文件中读取，做参数化使用，所以动态使用 
"""







