#!/usr/bin/env python 
# coding:utf-8
# @Time :1/2/19 08:56

from mongoengine import connect

connect("todo_list", host="127.0.0.1:27017")
