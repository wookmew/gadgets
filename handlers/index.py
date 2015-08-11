#coding:utf-8

import tornado.web
import BaseHandler import BaseHandler
import time
from application import application
from model.entity import Entity



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        conn = application.conn
        blogs = conn("select id from blog")
        self.render(
            "index.html",
            blogs = blogs,
            time = time,
            )

class EditHandler(tornado.web.RequestHandler):
    def get(self, id = None):
        blog = dict()
        if id:
            conn = application.conn
            blog = conn.findone({"id": int(id)})
            self.render("edit.html",
                blog = blog)

    def post(self, id = None):
        conn = application.conn
        blog = dict()
        if id:
            blog = conn.findone({"id": int(id)})
        blog['title'] = self.get_argument("title", None)
        blog['content'] = self.get_argument("content", None)
        if id:
            conn.save(blog)
        else:
            last = conn.find().sort("id").limit(1)
            lastone = dict()
            for item in last:
                lastone = item
            blog['id'] = int(lastone['id']) + 1
            blog['date'] = int(time.time())
            conn.insert(blog)
        self.redirect("/")


class DelHandler(tornado.web.RequestHandler):
    def get(self, id = None):
        conn = application.conn
        if id:
            blog = conn.findone({"id": int(id)})
            self.render("/" )

class BlogHandler(tornado.web.RequestHandler):
    def get(self, id = None):
        conn = application.conn
        if id:
            blog = conn.findone({"id": int{id}})
            self.render("blog.html",
                page_title = "my_blog",
                time = time
                )
        else:
            self.redirect("/")
            

