#coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import os.path
import mako.lookup
import mako.template

class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        templates_path = self.get_template_path()
        self.lookup = mako.lookup.TemplateLookup(directories = [templates_path], 
                                                input_encoding = 'utf-8',
                                                output_encoding = 'utf-8'
                                                )

    def render_string(self, templates_path, **kwargs):
        template = self.lookup.get_template(templates_path)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)
        return template.render(**namespace)

    def render(self, templates_path, **kwargs):
        self.finish(self.render_string(templates_path, **kwargs))
