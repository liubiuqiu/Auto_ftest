#导包 unittest ApiChannels
import unittest
from api.api_channels import ApiChannels
#读取数据 导入包
from parameterized import parameterized
from tools.read_json import ReadJson
#读取数据函数
def get_data():
    data = ReadJson("channels.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("expect_result"),
                 data.get("status_code")
                 ))
    return arrs
#新建测试类 继承
class TestChennels(unittest.TestCase):
    @parameterized.expand(get_data())
    #新建测试方法
    def test_channels(self,url,headers,expect_result,status_code):
        #临时数据
        # url = "https://www.lagou.com/jobs/mList.html"
        # headers = {"Conent-Type":"value","Authorization":"Beare token信息"}
        # 调用方法 获取频道信息
        t= ApiChannels().api_get_channels(url,headers)
        #调试打印结果
        print(t.json())
        #断言 状态码
        # self.assertEquals(200,t.status_code)
        #使用参数化
        self.assertEquals(status_code, t.status_code)
        #断言 响应信息
        # self.assertEquals("ok",t.json()["message"])
        #使用参数化
        self.assertEquals(expect_result, t.json()["message"])

if __name__ == '__main__':
    unittest.main()





