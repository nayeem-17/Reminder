from database.models.user_info import User_Info
from mongoengine.connection import disconnect
from database.models.logs import Logs
from mongoengine import connect
import os


def create_connection():
    """ create a database connection to a MongoDB Atlas """

    client = connect(
        host=os.getenv('MONGO_URL'),
    )
    print(client)


def post_exist(post_id):
    post_id = '519026101914218_1069166263566863'
    data = Logs.objects(post_id=post_id)
    print(data.to_json())
    if len(data) == 0:
        return False
    return True


def insert_item(course_no, post_id, post):
    data = Logs(post_id=post_id, post=post, course_no=course_no).save()
    print(data)


def close_connection():
    disconnect()
