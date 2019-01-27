#!/usr/bin/env python 
# coding:utf-8
# @Time :1/2/19 08:57

import sys
sys.path.append("..")

from mongoengine import Document
from mongoengine import (StringField, ListField, IntField, ReferenceField)

from .model_user import ModelUser
from datetime import datetime


class ModelTask(Document):

    meta = {"collection": "task"}
    _in_time = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=True)
    _utime = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=True)
    task = StringField(default="", required=True)
    start_time = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=True)
    end_time = StringField(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), required=True)
    repeat = ListField(StringField(required=True))
    delete_flag = IntField(default=0, required=True)
    user = ReferenceField(ModelUser, required=True)


