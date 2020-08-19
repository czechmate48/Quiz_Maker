#temp.py
'''This file holds temporary information needed by the program during
execution. It is instantiated when the program starts, and is deleted
when the program is closed'''

from dataclasses import dataclass

path="/home/czechmate/Documents/python/programs/Quiz_Maker"

@dataclass
class Data_Cat():

    uid: str="uid"

class Temp_Data():

    data={}

    @classmethod
    def store(cls,category,value):
        cls.create_dataspace(category,value)
        cls.add_value_to_dataspace(category,value)

    @classmethod
    def create_dataspace(cls,category,value):
        if data[category] not in data.values():
            data[category]=[]

    @classmethod
    def add_value_to_dataspace(cls,category,value):
        data[category].add(value)

    @classmethod
    def read(cls):
        pass

    @classmethod
    def match(cls,category,value):
        for data in data[category]:
            if data==value:
                return True
        return False

class Unique_Id():

    def __init__(self,uid=0):
        self.uid=uid
        self.uid=self.generate_uid(self.uid)
        self.store(self.uid)

    def generate_uid(self,uid):
        while Temp_Data.match(Data_Cat.uid,_uid):
            increment_uid(_uid)

    def increment_uid(self,_uid):
        _uid = _uid+1
        return _uid

    def store(self,_uid):
        Temp_Data.store(Data_Cat.uid,_uid)
