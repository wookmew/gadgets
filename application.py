#coding:utf-8

from urls import urls
import torndb
import tornado.web
import os
import conf

SETTINGS = dict(
    template_path = os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    )

application = tornado.web.Application(
    handlers = urls,
    **SETTINGS
    )

conn = torndb.Connection(host = conf.db['host'], 
                        database = conf.db['db'],
                        user = conf.db['user'],
                        password = conf.db['pass'])
