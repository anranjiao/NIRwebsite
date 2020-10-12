from flask import Flask, jsonify
from nirdata import Nir

"""
接口说明：
1. 返回json数据
2.结构
{
    resCode:0 #非零即错误
    data: #数据位置，一般为数组
    message：'对本次请求的说明'
}
"""

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False #编码能显示中文

@app.route('/nirs_cates', methods = ['GET'])
def get_nirs_cates():
    resData = {
        "resCode": 0,
        "data": [
            {"id":0,"text":'首页',"url":'/'},
            {"id":1,"text":'数据分析',"url":'/analysis'},
            {"id":2,"text":'产品购买',"url":'/products'},
            {"id":3,"text":'学习专区',"url":'/learn'},
            {"id":4,"text":'联系我们',"url":'/contact'},
            {"id":5,"text":'个人中心',"url":'/user'},
        ],
    "message": '对本次请求的说明'
    }
    return jsonify(resData)


@app.route('/', methods = ['GET','POST'])
def hello_world():
    nir = Nir()
    arrData = nir.get_customers_infos_limit()
    print(arrData)
    return jsonify(arrData)

if __name__ == "__main__":
    app.run(host = "localhost", port = 1943, debug = True)