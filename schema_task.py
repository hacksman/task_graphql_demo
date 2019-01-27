#!/usr/bin/env python 
# coding:utf-8
# @Time :1/2/19 09:02

from database.model_task import ModelTask
from graphene_mongo import MongoengineObjectType

import graphene
import schema_user

from datetime import datetime


class TaskAttribute:
    id = graphene.ID()
    _in_time = graphene.String()
    _utime = graphene.String()
    task = graphene.String()
    start_time = graphene.String()
    end_time = graphene.String()
    repeat = graphene.List(graphene.String)
    delete_flag = graphene.Int()
    user = graphene.String()


class Task(MongoengineObjectType):

    class Meta:
        model = ModelTask


class TaskNode(MongoengineObjectType):
    class Meta:
        model = ModelTask
        interfaces = (graphene.relay.Node, )


class CreateTaskInput(graphene.InputObjectType, TaskAttribute):
    pass


class CreateTask(graphene.Mutation):

    task = graphene.Field(lambda: TaskNode)

    class Arguments:
        input = CreateTaskInput(required=True)

    def mutate(self, info, input):
        task = ModelTask(**input)
        task.save()
        return CreateTask(task=task)


class UpdateTask(graphene.Mutation):

    task = graphene.Field(lambda: TaskNode)

    class Arguments:
        input = CreateTaskInput(required=True)

    def mutate(self, info, input):
        id = input.pop("id")
        task = ModelTask.objects.get(id=id)
        task._utime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task.update(**input)
        task.save()
        return UpdateTask(task=task)


