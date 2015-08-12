#coding:utf-8

from handlers.index import MainHandler, EditHandler, DelHandler, BlogHandler

urls = [
    (r'/', MainHandler),
    (r'edit/([0-9Xx\-]+)', EditHandler),
    (r'/add', EditHandler),
    (r'/delete/([0-9Xx\-]+)', DelHandler),
    (r'/blog/([0-9Xx\-]+)', BlogHandler),
]
