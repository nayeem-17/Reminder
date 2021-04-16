from mongoengine.document import EmbeddedDocument
from mongoengine.fields import EmailField, ListField, StringField


class Course_info(EmbeddedDocument):
    course_name = StringField(required=True)
    user_emails = ListField(EmailField())
