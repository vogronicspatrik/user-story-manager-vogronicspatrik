from base_model import *


class Sprint(BaseModel):
    sprint_id = PrimaryKeyField()
    title = CharField()
    user_story = CharField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()
