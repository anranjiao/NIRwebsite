from flask import Flask, jsonify
from nirdata import Nir

"""
接口说明：
1. 返回json数据
2.结构
{
    resCode:0 #非零即错误
    data: #数据位置，一般为数组
    message：‘对本次请求的说明’
}
"""

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False #编码能显示中文

@app.route('/', methods = ['GET','POST'])
def hello_world():
    nir = Nir()
    arrData = nir.get_customers_infos_limit()
    print(arrData)
    return jsonify(arrData)

if __name__ == "__main__":
    app.run(host = "localhost", port = 8000, debug = True)