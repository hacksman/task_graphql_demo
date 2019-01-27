#!/usr/bin/env python 
# coding:utf-8
# @Time :1/2/19 09:02

import schema_user
import schema_task
import graphene
from graphene_mongo.fields import MongoengineConnectionField


class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()

    tasks = MongoengineConnectionField(schema_task.TaskNode)

    users = MongoengineConnectionField(schema_user.UserNode)


class Mutation(graphene.ObjectType):
    create_task = schema_task.CreateTask.Field()
    create_user = schema_user.CreateUser.Field()

    update_user = schema_user.UpdateUser.Field()
    update_task = schema_task.UpdateTask.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
