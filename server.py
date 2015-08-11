#coding:utf-8

import tornado.ioloop
import sys
import tornado.options
from  tornado.options import define, options
import tornado.httpserver
from application import application

define("port", default = 8006, help = "run on the given port", type = int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server. listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
