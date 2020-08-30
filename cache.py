#cache.py
'''This file holds temporary information needed by the program during
execution. It is instantiated when the program starts, and is deleted
when the program is closed'''

from dataclasses import dataclass
from keys import Keys

path="/home/czechmate/Documents/python/programs/Quiz_Maker"

@dataclass
class Cache_Cat(Keys):

    uid: str="uid"
    question: str="question"
    quiz: str="quiz"

    @staticmethod
    def get_keys():
        k=Cache_Cat()
        return [k.__dict__[var] for var in k.__dict__]

class Container():
    '''This class holds all of the caches in the program. The variable 'caches' is a dictionary
    that holds lists. Each list is a cache and is identified by its corresponding key.'''

    caches={}

    @classmethod
    def store(cls,category,value):
        cls.create_cache(category) #if cache already exists this expression does nothing
        if value not in cls.caches[category]:
            cls.caches[category].append(value)

    @classmethod
    def create_cache(cls,category):
        if not cls.cache_exists(category):
            cls.caches[category]=[]

    @classmethod
    def get_cache(cls,category):
        return cls.caches[category]

    @classmethod
    def delete(cls,category,value):
        if not cls.cache_exists(category):
            print("cache does not exist")
        elif value not in cls.caches[category]:
            print("value not in cache")
        else:
            cls.caches[category].remove(value)
   
    @classmethod
    def cache_exists(cls,category):
        if category in cls.caches:
            return True
        return False

    @classmethod
    def match(cls,category,value):
        if cls.cache_exists(category):
            for item in cls.caches[category]:
                if item==value:
                    return True
        return False

###################

class Cacheable():
  
    @classmethod
    def create(cls,category):
        Container.create_cache(category)

    @classmethod
    def add(cls,category,value):
        Container.store(category,value)

    @classmethod
    def remove(cls,category,value):
        Container.delete(category,value)

    @classmethod
    def get_all(cls,category):
        return [item for item in Container.get_cache(category)]

    @classmethod
    def print_cache(cls,category):
        cache=Container.get_cache(category)
        for item in cache:
            print(item)

class Unique_Id(Cacheable):

    '''Unique_Id is a special cache that does not need to be 
    instantiated at program execution'''

    @classmethod
    def generate_uid(cls,_uid):
        while Container.match(Cache_Cat.uid,_uid):
            _uid=cls.increment_uid(_uid)
        cls.add(Cache_Cat.uid,_uid)
        return _uid

    @classmethod
    def increment_uid(cls,_uid):
        _uid = _uid+1
        return _uid

class Question_Cache(Cacheable):

    @classmethod
    def print_cache(cls,category=Cache_Cat.question):
        cache=Container.get_cache(category)
        for item in cache:
            print(item.content)

class Quiz_Cache(Cacheable):

    @classmethod
    def print_cache(cls,category=Cache_Cat.quiz):
        cache=Container.get_cache(category)
        for item in cache:
            print(item.content)
