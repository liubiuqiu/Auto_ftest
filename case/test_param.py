"""

安装：pip install parameterized
使用：
    @parameterized.expand(参数)
    参数：
    单个参数格式：列表，如 [值1，值2]
    多个参数：列表套元祖 如[(参考值1，参考值2)]
    需求：
    输出用户名和密码，数据为：1. admin,123456 2. user002,653421
"""

#导包
import unittest
from parameterized import parameterized

#新建测试类
class testpara(unittest.TestCase):
    # 新建测试方法
    @parameterized.expand([("admin","123456"),("user001","654321")])
    def test_para(self,username,password):
        print("用户名",username)
        print("密码",password)
