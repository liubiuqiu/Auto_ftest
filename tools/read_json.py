# 导包 json
import json
#打开json文件并获取文件流
# with open("../data/login.json", "r",encoding="utf-8") as f:
#     # 调用load方法加载文件流
#     data = json.loads(f)
#     print("获取数据为：", data)

#使用函数进行封装
# def read_json():
#     with open("../data/login.json", "r",encoding="utf-8") as f:
#         # 调用load方法加载文件流
#         return json.loads(f)

#使用参数替换 静态文件名
class ReadJson (object):
    def __init__(self, filename):
        self.filepath = "../data/" +filename
    def read_json(self):
        with open(self.filepath,"r",encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)

if __name__ =="__main__":
    # print(ReadJson("login.json").read_json())
    #登录信息调试
    # data = ReadJson("login.json").read_json()
    # arrs=[]
    # arrs.append((data.get("url"),
    #              data.get("mobile"),
    #              data.get("code"),
    #              data.get("expect_result"),
    #              data.get("status_code")
    #             ))
    # print(arrs)
    #获取用户列表信息调试
    # data = ReadJson("channels.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("expect_result"),
    #              data.get("status_code")
    #              ))
    # print(arrs)

    #获取文章收藏信息调试
    # data = ReadJson("article_add.json").read_json()
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("data"),
    #              data.get("expect_result"),
    #              data.get("status_code")
    #              ))
    # print(arrs)

    data = ReadJson("article_cancle.json").read_json()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")
                 ))
    print(arrs)