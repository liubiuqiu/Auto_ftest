#导包
import requests
#新建对象类
class ApiChannels(object):

    # 新建获取用户频道列表方法
    def api_get_channels(self,url,headers):
        # headers 定义
        headers = {"Conent-Type": "value"}
        #调用get 方法返回响应对象
        return requests.get(url,headers=headers)

"""
提示：url,heades 都是通过参数传递过来的
"""



