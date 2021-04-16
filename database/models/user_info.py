from database.models.course_info import Course_info
from mongoengine.document import Document
from mongoengine.fields import EmbeddedDocumentField, ListField


class User_Info(Document):
    info = ListField(EmbeddedDocumentField(Course_info))
