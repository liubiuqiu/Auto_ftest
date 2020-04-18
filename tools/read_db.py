#导包
import pymysql
#新建工具类数据库
class ReadDB:
    #定义链接对象 类方法
    conn =None
    #获取链接对象方法封装
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect("127.0.0.1",
                                   "roor",
                                   "123456",
                                   "lbq",
                                   Charset="utf8")
        #返回链接对象
        return self.conn
    #获取游标对象方法封装
    def get_cursor(self):
        return self.conn().cursor()
    #关闭游标对象方法封装
    def colse_cursor(self,cursor):
        if cursor:
            cursor.colse()
    #关闭链接对象方法封装
    def colse_conn(self):
        if self.conn:
            self.conn.close()
            #关闭后，需手工设置为None
            self.conn = None
    #主方法 外界用此方法就可以完成对应的数据库操作
    def get_sql_one(self,sql):
        #定义游标对象及数据变量
        sursor= None
        data = None
        try:
            #获取游标对象
            sursor=self.get_cursor
            #调用执行方法
            sursor.execute(sql)
            #获取结果
            data =sursor.fetchone()
        except Exception as e:
            print("get_sql_one error",e)
        finally:
            #关闭游标对象
            self.colse_cursor(sursor)
            #关闭链接对象
            self.colse_conn()
            #返回执行结果
        return data

    #获取所有数据结果集
    def get_sql_all(self,sql):
        # 定义游标对象及数据变量
        sursor = None
        data = None
        try:
            # 获取游标对象
            sursor = self.get_cursor
            # 调用执行方法
            sursor.execute(sql)
            # 获取所有结果
            data = sursor.fetchall()
        except Exception as e:
            print("get_sql_one error", e)
        finally:
            # 关闭游标对象
            self.colse_cursor(sursor)
            # 关闭链接对象
            self.colse_conn()
            # 返回执行结果
        return data
    #修改，删除，新增
    def update_sql(self,sql):
        # 定义游标对象及数据变量
        sursor = None
        data = None
        try:
            #获取游标对象
            sursor = self.get_cursor
            # 调用执行方法
            sursor.execute(sql)
            #提交事务
            self.conn.commit()
        except Exception as e:
            #事务回滚
            self.conn.rollback()
            print("get_sql_one error", e)
        finally:
            # 关闭游标对象
            self.colse_cursor(sursor)
            # 关闭链接对象
            self.colse_conn()
