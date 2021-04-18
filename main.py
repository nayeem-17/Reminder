from email_sender import *
from database.dbservice import create_connection, insert_item, post_exist
from database.models.course_info import Course_info
from database.models.user_info import User_Info
from fgraph import *
from dotenv import load_dotenv
import json
import time

load_dotenv()


def send_to_course_users(user_info, course_name, post):

    users_info = User_Info.objects()
    for course in users_info:
        if course_name == course_name:
            emails = course[course_name]
            for email in emails:
                send_email(receiver_email=email,
                           subject=course_name, message=main_post)
        else:
            break
        break


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
                    print(post)
                    if post['message'].find(course['course_name']) != -1:
                        main_post = post['message']
                        main_post += '\n'
                        if len(post) == 3:
                            attachment = 'Attched pictures\n'
                            attachment += posts['full_picture']
                        main_post += attachment
                        main_post += '\n'
                        main_post += ('Post link '+posts['permalink_url'])
                        print(main_post)
                        insert_item(
                            course_no=course['course_name'], post_id=posts['id'], post=main_post)
                        send_to_course_users(
                            user_info=users, course_name=course['course_name'], post=main_post)
            else:
                break
        break
        time.sleep(1800)
