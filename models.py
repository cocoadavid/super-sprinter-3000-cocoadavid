from peewee import *
from connect_database import ConnectDatabase


class BaseModel(Model):

    class Meta:
        database = ConnectDatabase.db


class UserStory(BaseModel):
    story_title = CharField(null=True)
    user_story = CharField(null=True)
    acceptance_criteria = CharField(null=True)
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()