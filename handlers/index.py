#coding:utf-8

import tornado.web 
from BaseHandler import BaseHandler
from model import MongoConnect

class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html',
                   page_title = "Burt's Books | Home",
                   header_text = "Welcome to Burt's Books!",) 



