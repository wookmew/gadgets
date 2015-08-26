#coding:utf-8

import tornado.web 
from BaseHandler import BaseHandler
from model.entity import Entity

class MainHandler(BaseHandler):
    def get(self):
        entity = Entity.get('J_blue\'s blog')
        self.render('index.html', entity = entity) 

