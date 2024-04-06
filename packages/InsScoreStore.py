import redis
import os
from dotenv import load_dotenv

load_dotenv()

SET_NAME = os.environ["REDIS_SET_NAME"]

redis_client = redis.Redis(host='localhost', port=os.environ["REDIS_CONTAINER_PORT"], db=0)

def addElement(key, value):
    redis_client.zadd(SET_NAME, {key: value})

# def getAllElement()
# # Retrieving elements
# print(redis_client.zrange('my_sorted_set', 0, -1, withscores=True))

# Incrementing the score of an element
# redis_client.zincrby('my_sorted_set', 1, 'Alice')

# Getting the rank of an element
# print(redis_client.zrank('my_sorted_set', 'Alice'))

# Removing elements
# redis_client.zrem('my_sorted_set', 'Charlie')

# def removeKey(key, ):