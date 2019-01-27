#!/usr/bin/env python 
# coding:utf-8
# @Time :1/2/19 09:02

from database.model_user import ModelUser
from graphene_mongo.types import MongoengineObjectType
import graphene
from datetime import datetime


class UserAttribute:
    id = graphene.String()
    _in_time = graphene.String()
    _utime = graphene.String()
    nickname = graphene.String()
    photo = graphene.String()
    sex = graphene.String()
    delete_flag = graphene.Int()


class User(MongoengineObjectType):

    class Meta:
        model = ModelUser


class UserNode(MongoengineObjectType):

    class Meta:
        model = ModelUser
        interfaces = (graphene.relay.Node, )


class CreateUserInput(graphene.InputObjectType, UserAttribute):
    pass


class CreateUser(graphene.Mutation):

    user = graphene.Field(lambda: UserNode)

    class Arguments:
        input = CreateUserInput(required=True)

    def mutate(self, info, input):
        user = ModelUser(**input)
        user.save()
        return CreateUser(user=user)


class UpdateUser(graphene.Mutation):

    user = graphene.Field(lambda: UserNode)

    class Arguments:
        input = CreateUserInput(required=True)

    def mutate(self, info, input):
        id = input.pop("id")
        user = ModelUser.objects.get(id=id)
        user._utime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user.update(**input)
        user.save()
        return UpdateUser(user=user)

