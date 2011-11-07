#!/usr/bin/env python
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo
from tornado.options import define, options
import json
import uuid
import dboperator
import os.path

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #self.render("index.html")
	self.redirect("/name")

class NameHandler(tornado.web.RequestHandler):
	def get(self):
		self.dbase = dboperator.Dboperator()
		stra = list(self.dbase.getAllDatafromBase())
		self.render("home.html", entries=stra)

class ArchiveHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Good")

	def post(self):
		self.dbase = dboperator.Dboperator()
		uuid=self.get_argument("uuid")
		self.dbase.removeDatafromBase({"uuid":uuid})
		self.redirect("/name")

class RemoveHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("remove")

class MainPageHandler(tornado.web.RequestHandler):
	def get(self):
		self.dbase = dboperator.Dboperator()
		stra = list(self.dbase.getAllDatafromBase())
		l=len(stra)/2
		entries=[]
		entries1=[]
		for i in range(l):
			entries.append(stra[i])
			entries1.append(stra[i+l])
		#handler data for outputing
		self.render("index.html", entries=entries, entries1=entries1)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/", MainHandler),
			(r"/name", NameHandler),
			(r"/archive", ArchiveHandler),
			(r"/remove", RemoveHandler),
			(r"/main", MainPageHandler)
		    ]
		settings = dict(
			template_path=os.path.join(os.path.dirname(__file__), "templates"),
            		static_path=os.path.join(os.path.dirname(__file__), "static"),
           		ui_modules={"Entry": MainHandler},
		)

	        tornado.web.Application.__init__(self, handlers, **settings)

	        ## Have one global connection to the blog DB across all handlers
	        #self.db = tornado.database.Connection(
	        #    host=options.mysql_host, database=options.mysql_database,
	        #   user=options.mysql_user, password=options.mysql_password)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
