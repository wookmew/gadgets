#coding:utf-8

import asyncmongo

class MongoConnect:

    def mongoCon(self):
        self.db = asyncmongo.Client(host = '127.0.0.1', port = 27017, maxcached = 10, maxconnection = 50, dbname='test')

