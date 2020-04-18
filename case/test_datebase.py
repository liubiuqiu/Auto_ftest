#导包
import pymysql

#获取链接对象
conn = pymysql.connect("127.0.0.1",
                       "roor",
                       "123456",
                       "lbq",
                       Charset="utf8")
#获取游标对象
cursor =conn.cursor()
#执行方法"sql"
sql = "select a from lbq where user_id=12 "
#获取结果并进行断言 0 收藏
# print(cursor.fetchone())
result = cursor.fetchone()
#断言
assert 0 == result[0]
#关闭游标对象
cursor.close()
#关闭链接对象
conn.close()
