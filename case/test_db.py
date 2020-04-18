#导包
import unittest
from tools.read_db import ReadDB

#新建测试类 继承
class TestDB(unittest.TestCase):
    #新建测试方法
    def test_db(self):
        #定义sql语句
        sql = "select a from lbq where user_id=12 "
        #调用get_sql_one 方法
        data = ReadDB().get_sql_one(sql)
        print(data)
        #断言
        self.assertEquals(0,data[0])

if __name__ == '__main__':
    unittest.main()