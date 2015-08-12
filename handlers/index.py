#coding:utf-8

import tornado.web
import BaseHandler
import time
import pymongo
import application
from model.entity import Entity


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        conn = application.db.demo
        blogs = conn.find().sort("id", pymongo.DESCENDING)
        self.render(
            "index.html",
            blogs = blogs,
            time = time,
            )

class EditHandler(tornado.web.RequestHandler):
    def get(self, id = None):
        blog = dict()
        #因为id = None，所以if id:为false。因此接下来执行self.render("edit.html",blog = blog)。
        if id:
            conn = application.db.demo
            blog = conn.find_one({"id": int(id)})
            self.render("edit.html",
                blog = blog)

    def post(self, id = None):
        conn = application.db.demo
        blog = dict()
        if id:
            blog = conn.find_one({"id": int(id)})
        blog['title'] = self.get_argument("title", None)
        blog['content'] = self.get_argument("content", None)
        if id:
            conn.save(blog)
        else:
            last = conn.find().sort("id", pymongo.DESCENDING).limit(1)
            lastone = dict()
            for item in last:
                lastone = item
            blog['id'] = int(lastone['id']) + 1
            blog['date'] = int(time.time())
            conn.insert(blog)
        self.redirect("/")


class DelHandler(tornado.web.RequestHandler):
    def get(self, id = None):
        conn = application.db.demo
        if id:
            blog = conn.remove({"id": int(id)})
            self.render("/" )

class BlogHandler(tornado.web.RequestHandler):
    def get(self, id = None):
        conn = application.db.demo
        if id:
            blog = conn.find_one({"id": int(id)})
            self.render("blog.html",
                page_title = "my_blog",
                blog = blog,
                time = time,
                )
        else:
            self.redirect("/")
            

