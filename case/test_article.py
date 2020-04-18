#导包 unittest ApiArticle
import unittest
from api.api_artice import ApiArticle

from parameterized import parameterized
from tools.read_json import ReadJson
#读取收藏数据函数
def get_data_add():
    data = ReadJson("article_add.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")
                 ))
    return arrs

def get_data_cancle():
    data = ReadJson("article_cancle.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")
                 ))
    return (arrs)

#新建测试类 继承
class TestArticle(unittest.TestCase):
    @parameterized.expand(get_data_add())
    #新建测试方法
    def test01_collection(self,url,headers,data,expect_result,status_code):
        #临时数据
        # url = "https://www.lagou.com/jobs/mList.html"
        # headers = {"Conent-Type":"value","Authorization":"Beare token信息"}
        # data = {"target":1}
        #调用收藏文章方法
        t= ApiArticle().api_post_article(url,headers,data)
        #调试数据查看
        print("响应数据数据",t.json())
        #断言 响应信息
        self.assertEquals(expect_result,t.json()["message"])
        #断言 状态码
        self.assertEquals(status_code,t.status_code)
    # 新建测试方法
    @parameterized.expand(get_data_cancle())
    def test01_cancle(self,url,headers,status_code):
        # 临时数据
        # url = "https://www.lagou.com/jobs/mList.html"
        # headers = {"Conent-Type":"value","Authorization":"Beare token信息"}
        # 调用收藏文章方法
        t= ApiArticle().api_delete_article(url,headers)
        #调试数据打印查看
        print(t.json())
        # 断言 状态码
        self.assertEquals(status_code,t.status_code)
if __name__ == '__main__':
    unittest.main()