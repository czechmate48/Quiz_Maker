# cache.py
"""This file holds temporary information needed by the program during
execution. It is instantiated when the program starts, and is deleted
when the program is closed"""
import random
from dataclasses import dataclass

from elements.keys import Keys


@dataclass
class CacheCat(Keys):
    uid: str = "uid"
    question: str = "question"
    quiz: str = "quiz"
    answer_sheet: str = "answer sheet"

    @staticmethod
    def get_keys():
        k = CacheCat()
        return [k.__dict__[var] for var in k.__dict__]


class Container:
    """This class holds all of the caches in the program. The variable 'caches' is a dictionary
    that holds lists. Each list is a cache and is identified by its corresponding key."""

    caches = {}

    @classmethod
    def store(cls, cache_name, value):
        cls.create_cache(cache_name)  # if cache already exists this expression does nothing
        if value not in cls.caches[cache_name]:
            cls.caches[cache_name].append(value)

    @classmethod
    def create_cache(cls, cache_name):
        if not cls.cache_exists(cache_name):
            cls.caches[cache_name] = []

    @classmethod
    def get_cache(cls, cache_name):
        return cls.caches[cache_name]

    @classmethod
    def delete_value(cls, cache_name, value):
        if not cls.cache_exists(cache_name):
            print("cache does not exist")
        elif value not in cls.caches[cache_name]:
            print("value not in cache")
        else:
            cls.caches[cache_name].remove(value)

    @classmethod
    def delete_cache(cls, cache_name):
        if cls.cache_exists(cache_name):
            cls.caches.pop(cache_name)

    @classmethod
    def cache_exists(cls, cache_name):
        if cache_name in cls.caches:
            return True
        return False

    @classmethod
    def match(cls, cache_name, value):
        if cls.cache_exists(cache_name):
            for item in cls.caches[cache_name]:
                if item == value:
                    return True
        return False


class Cacheable:

    @classmethod
    def create_cache(cls, cache_name):
        Container.create_cache(cache_name)

    @classmethod
    def add_value_to_cache(cls, cache_name, value):
        Container.store(cache_name, value)

    @classmethod
    def delete_cache(cls, cache_name):
        Container.delete_cache(cache_name)

    @classmethod
    def remove_value_from_cache(cls, cache_name, value):
        Container.delete_value(cache_name, value)

    @classmethod
    def get_all_values_in_cache(cls, cache_name):
        return [item for item in Container.get_cache(cache_name)]

    @classmethod
    def print_cache(cls, cache_name):
        cache = Container.get_cache(cache_name)
        for item in cache:
            print(item)


class UniqueId(Cacheable):
    """Unique_Id is a special cache that does not need to be
    instantiated at program execution"""

    @classmethod
    def generate_uid(cls, _uid):
        while Container.match(CacheCat.uid, _uid):
            _uid = cls.increment_uid(_uid)
        cls.add_value_to_cache(CacheCat.uid, _uid)
        return _uid

    @classmethod
    def increment_uid(cls, _uid):
        _uid = _uid + 1
        return _uid


class QuestionCache(Cacheable):

    @classmethod
    def print_cache(cls, category=CacheCat.question):
        cache = Container.get_cache(category)
        for item in cache:
            print(item.content)

    @classmethod
    def randomize(cls, category=CacheCat.question):
        cache = Container.get_cache(category)
        random.shuffle(cache)


class QuizCache(Cacheable):

    @classmethod
    def print_cache(cls, category=CacheCat.quiz):
        cache = Container.get_cache(category)
        for item in cache:
            print(item.content)


class AnswerSheetCache(Cacheable):

    @classmethod
    def print_cache(cls, category=CacheCat.answer_sheet):
        cache = Container.get_cache(category)
        for item in cache:
            print(item.content)
