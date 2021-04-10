import os
from facebook import GraphAPI
from dotenv import load_dotenv

load_dotenv()

graph = GraphAPI(access_token=os.getenv('ACCESS_TOKEN'))
fields = ['first_name', 'id', 'name']
print(os.getenv('ACCESS_TOKEN'))

profile = graph.get_object('me', fields=fields)

print(profile)
