#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from flask import Flask
from Users.API import init_user_api
from News.API import init_news_api
from constant import MAX_USER, students
# sys.path.append('./API/')
app = Flask(__name__)
app.debug = True

# register multiple modules
init_user_api(app)
init_news_api(app)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
