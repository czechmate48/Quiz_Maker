#question.py
'''Creates a question object that contains a variable for
each component of a question. Note that the question object
does NOT produce a dictionary by default, and will need to 
be converted to  a dictionary using the built in method'''

from menu import Menu_Factory,Option_Factory
from dataclasses import dataclass
from file_manager import File_Writer, File_Reader
from cache import Unique_Id
import ast

#######################

@dataclass
class Question_Styles():
    '''This class holds the various types of styles a question can be.
    Extend class and just add values as needed for new styles'''
    
    true_false: str="TRUE/FALSE"
    multiple_choice: str="MULTIPLE CHOICE"
    fill_in_the_blank: str="FILL IN THE BLANK"

    @staticmethod
    def get_styles():
        qs=Question_Styles()
        return [qs.__dict__[var] for var in qs.__dict__]

@dataclass
class Question_Keys():
    '''This class holds the standard keys used when creating questions.
    Extend class and just add values as needed for new keys'''

    uid: str="uid"
    style: str="style"
    inquiry: str="inquiry"
    choices: str="choices"
    answer: str="answer"

    @staticmethod
    def get_keys():
        qk=Question_Keys()
        return [qk.__dict__[var] for var in qk.__dict__]

class Question_IO(File_Writer,File_Reader):
   
    @classmethod
    def populate_cache(cls,_file_path):
        _lines = cls.get_lines(_file_path)
        _questions=[]
        for line in _lines:
            _questions.add(read_question_from_file(line,Question_Keys.get_keys))
        for question in _questions:
            Question_Cache.add(Cache_Cat,question)

    @classmethod
    def read_question_from_file(cls,_line,_qkeys):
        '''Get a question from a line in a text file.'''
        _raw_content=ast.literal_eval(_line)
        _qvalues=[]
        for key in _qkeys:
            _qvalues=_qvalues.append(_raw_content[key])
        return Question_Factory.create_question(_qvalues,_qkeys,False) #create a generic question
   
    @classmethod
    def append_question_to_file(cls,_file_path,_question):
        cls.write_line(_question.content,_file_path)

    @classmethod
    def prompt_remove_question(cls,_file_path):
        _questions = cls.get_values(Question_Keys.inquiry,_file_path)
        _options = Option.generate_value_options(_questions)
        _header = "\nWhich question would you like to delete?\n"
        _selection_message="\nPlease select a question\n"
        return Menu_Factory.run_option_menu(_options,_selection_message,_header)

#####################

class Question():
    '''Questions are created with a style, inquiry, choices, and an answer.
    Each question has a unique ID that may or may not be created at instantiation,
    depending upon whether the contents passed into the Question already have an ID'''

    def __init__(self, qvalues, qkeys, generate_id=True):
        self._values=[]
        self._keys=[]
        if generate_id:
            self.uid = id(self)
            self.uid = Unique_Id.generate_uid(self.uid)
            self._values.append(self.uid)
        for qvalue in qvalues:
            self._values.append(qvalue) 
        for qkey in qkeys:
            self._keys.append(qkeys)
        self.content=self.merge_input(qvalues,qkeys)

    def merge_input(self,qvalues,qkeys):
        _items=zip(qkeys,qvalues) 
        return {item[0]:item[1] for item in _items}

    def update(self,qvalues,qkeys,generate_id=False):
        self.__init__(qvalues,qkeys,generate_id)

    ##########################
    #Prompting for user input#
    ##########################

    @staticmethod
    def prompt_for_style():
        _options = Option_Factory.generate_unlinked_options(Question_Styles.get_styles())
        _selection_message = "\nPlease select a question style\n"
        _header="\nwhat is the question style?\n"
        _selected_option = Menu_Factory.run_option_menu(_options,_selection_message,_header)
        return _selected_option.display_value

    def prompt_for_inquiry(self):
        _header = "Please input a question"
        return Menu_Factory.run_no_option_menu(_header)

    def prompt_for_choices(self):
        return []

    def prompt_for_answer(self,_choices):
        _header = "Please input the answer"
        return Menu_Factory.run_no_option_menu(_header)

    def display():
        pass

###################
#QUESTION CHILDREN#
###################

class True_False(Question):
    
    def prompt_for_choices(self):
        return ["true","false"]

    def prompt_for_answer(self,_choices):
        _options=Option_Factory.generate_unlinked_options(_choices)
        _selection_message="\nSelect correct answer\n"
        _header="\nWhich choice is the correct answer?\n"
        _selected_option = Menu_Factory.run_option_menu(_options,_selection_message,_header)
        return _selected_option.display_value

class Fill_In_The_Blank(Question):
    pass

class Multiple_Choice(Question):
    
    def prompt_for_choices(self):
        _num_choices=self.get_num_choices()
        return self.get_choices_from_user(_num_choices)

    def get_num_choices(self):
        _num_choices = -1
        while _num_choices == -1:
            try:
                _header="Please  input the number of choices"
                _num_choices=Menu_Factory.run_no_option_menu(_header)
                _num_choices=int(_num_choices)
            except ValueError:
                _num_choices=-1
        return  _num_choices

    def get_choices_from_user(self,_num_choices):
        _choices=[]
        while _num_choices > 0:
            print("please input a choice")
            _choices.append(input())
            _num_choices-=1
        return _choices

    def prompt_for_answer(self,_choices):
        _options=Option_Factory.generate_unlinked_options(_choices)
        _selection_message="\nSelect correct answer"
        _header="\nWhich choice is the correct answer?\n"
        _selected_option=Menu_Factory.run_option_menu(_options,_selection_message,_header)
        return _selected_option.display_value

##################
#QUESTION FACTORY#
##################

class Question_Factory():

    @staticmethod
    def create_question(qstyle,qvalues=[],qkeys=Question_Keys.get_keys(),generate_key=True):
        if qstyle == Question_Styles.true_false:
            return Question_Factory.create_true_false_question(qvalues,qkeys,generate_key)
        elif qstyle == Question_Styles.multiple_choice:
            return Question_Factory.create_multiple_choice_question(qvalues,qkeys,generate_key)
        elif qstyle == Question_Styles.fill_in_the_blank:
            return Question_Factory.create_fill_in_the_blank_question(qvalues,qkeys,generate_key)
        else:
            return Question_Factory.create_generic_question(qvalues,qkeys,generate_key)

    @staticmethod
    def create_true_false_question(qvalues=[],qkeys=Question_Keys.get_keys(),generate_key=True):
        return True_False(qvalues,qkeys,generate_key)

    @staticmethod
    def create_multiple_choice_question(qvalues=[],qkeys=Question_Keys.get_keys(),generate_key=True):
        return Multiple_Choice(qvalues,qkeys,generate_key)

    @staticmethod
    def create_fill_in_the_blank_question(qvalues=[],qkeys=Question_Keys.get_keys(),generate_key=True):
        return Fill_In_The_Blank(qvalues,qkeys,generate_key)

    @staticmethod
    def create_generic_question(qvalues=[],qkeys=Question_Keys.get_keys(),generate_key=True):
        return Question(qvalues,qkeys,generate_key)
