#quiz.py

from file_manager import File_Writer,File_Reader 
from dataclasses import dataclass
from cache import Unique_Id, Cache_Cat, Quiz_Cache
from keys import Keys
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
    question_file: str="question_file"

    @staticmethod
    def get_keys():
        k=Quiz_Keys()
        return [k.__dict__[var] for var in k.__dict__]

class Quiz(Element):

    @staticmethod
    def prompt_for_style():
        _options = Option_Factory.generate_unlinked_options(Quiz_Styles.get_styles())
        _selection_message="\nPlease select a quiz style\n"
        _header="\nWhat is the quiz style?"
        _selected_option=Menu_Factory.run_option_menu(_options,_selection_message,_header)
        return _selected_option.display_value



    


