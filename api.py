#!/usr/bin/env python 
# coding:utf-8
# @Time :1/2/19 09:03

from flask import Flask
from schema import schema
from flask_graphql import GraphQLView
from database.base import connect
from logger import AppLogger

log = AppLogger("task_graphql.log").get_logger()


app = Flask(__name__)
app.debug = True


app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))


if __name__ == '__main__':
    app.run()

