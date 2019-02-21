#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb as mdb
db = 'dogs'
table = 'dog'
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': '123456789',
    'db': db,
    'charset': 'utf8'
}

useDB = 'USE ' + db
createTable = 'CREATE TABLE IF NOT EXISTS ' + table + '( \
    id INT NOT NULL AUTO_INCREMENT, \
    name VARCHAR(20), \
    borndate VARCHAR(20), \
    price VARCHAR(10) NOT NULL, \
   PRIMARY KEY ( id )\
) ENGINE = MyISAM CHARSET = utf8';


def init_db():
    conn = mdb.connect(**config)
    cur = conn.cursor()
    exec_sql(cur, useDB)
    exec_sql(cur, createTable)
    return cur


def exec_sql(cur, sql):
    if sql:
        print sql
        cur.execute(sql)
        return cur.fetchall()
    else:
        return None


def add_dog(name, borndate, price):
    # 字符串的话 value后面的%s 一定要转义
    sql = 'insert into %s(name, borndate, price) values (\'%s\', \'%s\' , \'%s\')' % (table, name, borndate, price)
    cur = init_db()
    ret = exec_sql(cur, sql)
    # 执行成功ret为空 如果报错 ret不为空
    if ret:
        return False
    else:
        return True
