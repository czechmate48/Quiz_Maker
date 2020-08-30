#quiz.py

from file_manager import File_Writer,File_Reader 
from dataclasses import dataclass
from cache import Unique_Id, Cache_Cat
from keys import Keys
from element import Element, Element_Factory
from menu import Menu,Menu_Factory,Option,Option_Factory
import ast

@dataclass
class Quiz_Styles(Keys):

    generic: str="generic"

    @staticmethod
    def get_styles():
        k=Quiz_Styles()
        return [k.__dict__[var] for var in k.__dict__]

@dataclass
class Quiz_Keys(Keys):
    
    uid: str="uid"
    name: str="name"
    style: str="style"
    question_file: str="question_file" #the name of the file that holds questions for the quiz

    @staticmethod
    def get_keys():
        k=Quiz_Keys()
        return [k.__dict__[var] for var in k.__dict__]

class Quiz(Element):

    @staticmethod
    def prompt_for_style():
        _options = Option_Factory.generate_unlinked_options(Quiz_Styles.get_styles())
        _header="Please select a quiz style"
        _selected_option=Menu_Factory.run_option_menu_no_sm(_options,_header)
        return _selected_option.display_value

    @staticmethod
    def prompt_for_name():
        _header="\nWhat is is the name of this quiz?"
        _selected_option=Menu_Factory.run_no_option_menu(_header)
        return _selected_option

    def get_name(self):
        return self.content[Quiz_Keys.name]

class Quiz_Factory(Element_Factory):
    pass

