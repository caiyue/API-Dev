#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import jsonify, request
from constant import students


def init_news_api(app):
    @app.route('/newslist', methods=['GET'])
    def newslist():
        return 'list is empty'




