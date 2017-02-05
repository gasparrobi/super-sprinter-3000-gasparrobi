from peewee import *

db = PostgresqlDatabase('robertgaspar', user='robertgaspar')


class BaseModel(Model):

    class Meta:
        database = db


class UserStoryManager(BaseModel):
    title = CharField()
    story = TextField()
    criteria = TextField()
    value = IntegerField()
    estimation = FloatField()
    status = CharField()

    class Meta:
        order_by = ('id', 'title')
