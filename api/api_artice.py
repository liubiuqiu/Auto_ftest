#导入包
import requests
#新建文件测试类
class ApiArticle(object):
    #新建文章收藏方法
    def api_post_article(self,url,headers,data):
        #调用post方法 返回响应数据
        return requests.post(url,headers=headers,json=data)
    #新建文章取消方法
    def api_delete_article(self,url,headers):
        # 调用delete方法 返回响应数据
        return requests.delete(url,headers=headers)
