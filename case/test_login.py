"""
目标：实现登陆接口封装
"""
#导入 unittest Apilogin 包
import unittest
from api.api_login import Apilogin

from parameterized import parameterized
from tools.read_json import ReadJson
#读取数据函数
def get_data():
    data = ReadJson("login.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("mobile"),
                 data.get("code"),
                 data.get("expect_result"),
                 data.get("status_code")
                 ))
    return arrs
#新建测试类
class TestLogin(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,expect_result,status_code):
        #临时存放数据 url，mobile，code
        # url ="https://www.lagou.com/jobs/mList.html"
        # mobile ="18263910266"
        # code ="888888"
        #调用登录方法
        s =Apilogin().api_login(url,mobile,code)

        """
        调试使用
        """
        print("查看响应信息", s.json())
        #断言 响应信息及状态码
        self.assertEquals(expect_result,s.json()["msg"])
        # 断言 响应状态码
        self.assertEquals(status_code,s.status_code)

if __name__ == '__main__':
    unittest.main()



