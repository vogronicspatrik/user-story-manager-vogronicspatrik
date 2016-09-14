from peewee import *

db = PostgresqlDatabase('patrik', user='patrik')


class BaseModel(Model):
    class Meta:
        database = db
        
