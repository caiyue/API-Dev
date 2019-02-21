#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import jsonify, request
from constant import students
from Model.db import exec_sql, add_dog


def init_user_api(app):

    @app.route('/<int:task_id>', methods=['GET'])
    def index(task_id):
        return task_id

    @app.route('/')
    def homepage():
        return jsonify(students)

    # ==================================================================
    # ==================================================================
    # TypeError: query_id() got an unexpected keyword argument 'query_id'
    # 这里的参数 query_id 以及方法里的形参必须要一模一样，不然会报上面的错误
    # 这里的query_id 是自动匹配到URL 中的path 参数，？后面的查询参数，需要其他方式来解析
    # 使用方式： 127.0.0.1/query/1000
    @app.route('/query/<int:query_id>', methods=['GET'])
    def query_id(query_id):
        name = request.args.get('name', type=str, default='')
        age = request.args.get('age', type=int, default=0)
        return jsonify({'name': name, 'age': age, 'id': query_id})

    # 带SQL
    @app.route('/dog_query', methods=['GET'])
    def dog_query():
        name = request.args.get('name', type=str, default='')
        borndate = request.args.get('borndate', type=str, default='')
        price = request.args.get('price', type=str, default='')
        ret = add_dog(name=name, borndate=borndate, price=price)
        if ret:
            return 'add Success'
        else:
            return 'Add failed'

    @app.route('/adduser/<int:userId>', methods=['POST'])
    def getUser(userId):
        user_name = request.form.get('user_name')
        user_password = request.form.get('user_password')
        user_nickname = request.form.get('user_nickname')
        user_email = request.form.get('user_email')

        if len(user_name) > 0 and len(user_password) > 0:
            return 'insert success'
        else:
            return 'insert failed'
    # ==================================================================
    # ==================================================================



