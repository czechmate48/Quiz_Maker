#cache.py
'''This file holds temporary information needed by the program during
execution. It is instantiated when the program starts, and is deleted
when the program is closed'''

from dataclasses import dataclass

path="/home/czechmate/Documents/python/programs/Quiz_Maker"

@dataclass
class Cache_Cat():

    uid: str="uid"
    question: str="question"

class Cache():

    data={}

    @classmethod
    def store(cls,category,value):
        cls.create_cache(category) #if cache already exists this expression does nothing
        if value not in cls.data[category]:
            cls.data[category].append(value)

    @classmethod
    def create_cache(cls,category):
        if not cls.cache_exists(category):
            cls.data[category]=[]

    @classmethod
    def delete(cls,category,value):
        if not cls.cache_exists(category):
            print("cache does not exist")
        elif value not in cls.data[category]:
            print("value not in cache")
        else:
            cls.data[category].remove(value)
   
    @classmethod
    def cache_exists(cls,category):
        if category in cls.data:
            return True
        return False

    @classmethod
    def match(cls,category,value):
        if cls.cache_exists(category):
            for item in cls.data[category]:
                if item==value:
                    return True
        return False

###################

class Cacheable():
    
    @classmethod
    def add(cls,category,value):
        Cache.store(category,value)

    @classmethod
    def remove(cls,category,value):
        Cache.delete(category,value)

class Unique_Id(Cacheable):

    @classmethod
    def generate_uid(cls,_uid):
        while Cache.match(Cache_Cat.uid,_uid):
            _uid=cls.increment_uid(_uid)
        cls.add(Cache_Cat.uid,_uid)
        return _uid

    @classmethod
    def increment_uid(cls,_uid):
        _uid = _uid+1
        return _uid

class Question_Cache(Cacheable):

    def __init__(self):
        pass

