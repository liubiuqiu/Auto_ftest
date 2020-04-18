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
    datas = ReadJson("login_more.json").read_json()
    #新建空列表，读取json数据
    arrs=[]
    #使用遍历获取所有的value值
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")
                    ))
    print(arrs)