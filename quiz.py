#quiz.py

from file_manager import File_Writer,File_Reader 
from dataclasses import dataclass
from cache import Unique_Id, Cache_Cat, Quiz_Cache
from keys import Keys
import ast

@dataclass
class Quiz_Keys(Keys):

    uid: str="uid"
    name: str="name"
    question_file: str="question_file"

class Quiz(Element):

    


