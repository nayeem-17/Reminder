import os
from facebook import GraphAPI

graph = GraphAPI(access_token=os.getenv('LONG_LIVED_ACCESS_TOKEN'))
fields = ["feed.limit(10){permalink_url,full_picture}"]
GROUP = os.getenv('GROUP_ID')


def get_feed():
    feed = graph.get_object(GROUP, fields=fields)
    return feed


def get_post(post_id):
    post = graph.get_object(post_id)
    return post
