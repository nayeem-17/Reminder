# from .emai_sender import email_sender
from database.dbservice import create_connection, post_exist
from database.models.course_info import Course_info
from database.models.user_info import User_Info
from fgraph import *
from dotenv import load_dotenv
import json
import time

load_dotenv()


def send_to_course_users(user_info, course_name, post):
    pass


def make_mail_body():
    pass


if __name__ == "__main__":

    # creating sent_post table
    create_connection()

    # fetching data of users
    users = json.loads(User_Info.objects()[0].to_json())

    while True:
        # do something
        feeds = get_feed()
        for posts in feeds['feed']['data']:
            if post_exist(posts['id']) == False:
                post = get_post(posts['id'])
                for course in users['info']:
                    if post['message'].find(course['course_name']) != -1:
                        main_post = post['message']

                        send_to_course_users(
                            user_info=users, course_name=course['course_name'], post=main_post)
            else:
                break
        time.sleep(1800)
