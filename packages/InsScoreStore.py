import redis
import os
from dotenv import load_dotenv
import random

load_dotenv()

# SET_NAME = os.environ["REDIS_SET_NAME"]


class RedisStore:

    def __init__(self, _setName) -> None:
        self.SET_NAME = _setName
        self._redis_client = redis.Redis(host='localhost', port=int(os.environ["REDIS_CONTAINER_PORT"]), db=0)


    def addElement(self, key, value):
        self._redis_client.zadd(self.SET_NAME, {key: value})

    def getElements(self):
        client = self._redis_client
        Ins_count = client.zcard(self.SET_NAME)
        top_Ins = list(client.zrevrange(self.SET_NAME, 0, 19, withscores=True))


        random_Ins = []
        if Ins_count > 20 : # if there are more than 20 elements, get the 3 random elements
            all_indices = list(range(Ins_count - 20))
            random_indices = random.sample(all_indices, min(3, len(all_indices)))
            for index in random_indices:
                random_element = list(client.zrange(self.SET_NAME, index, index, withscores=True))
                if random_element: random_Ins.extend(random_element)

        returnIns = [ *top_Ins, *random_Ins]
        return returnIns






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