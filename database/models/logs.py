from mongoengine.document import Document
from mongoengine.fields import DateTimeField, IntField, StringField
import datetime


class Logs(Document):
    time = DateTimeField(default=datetime.datetime.now())
    course_no = StringField()
    post_id = StringField(unique=True, required=True)
    post = StringField()
