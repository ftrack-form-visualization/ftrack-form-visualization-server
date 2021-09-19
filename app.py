# -*- coding: utf-8 -*-
"""
@author: LiaoKong
@time: 2021/09/19 22:15 
"""
from flask import Flask

from api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
