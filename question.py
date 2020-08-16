#question.py
'''Creates a question object that contains a variable for
each component of a question. Note that the question object
does NOT produce a dictionary by default, and will need to 
be converted to  a dictionary using the built in method'''

from menu import Menu_Factory,Option
from dataclasses import dataclass
from file_manager import File_Writer, File_Reader
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

class Question_Utility(File_Writer,File_Reader):

    @classmethod
    def get_all_question_values_by_key(cls,_key,_file_path):
        _lines=cls.get_lines(_file_path) 
        _questions = [cls.get_question_from_line(line,Question_Keys.get_keys()) for line in _lines]
        _questions_dict = [cls.get_question_as_dictionary(question) for question in _questions]
        _values = [question_dict[_key] for question_dict in _questions_dict]
        return _values

    @classmethod
    def get_question_from_line(cls,line,qkeys):
        '''Get a question from a line in a text file.
        The line must be saved in dictionary format
        as this method derives keys & values'''
        _raw_content=ast.literal_eval(line)
        _qvalues=[]
        for _key in qkeys:
            _qvalues.append(_raw_content[_key])
        return Question(_qvalues,qkeys)
   
    @classmethod
    def append_question_to_file(cls,_file_path,_question):
        _line = cls.get_question_as_dictionary(_question)
        cls.write_line(_line,_file_path)

    @classmethod
    def get_question_as_dictionary(cls,question):
        _items=zip(question._keys,question._values) 
        _line={}
        for item in _items:
            _line[item[0]]=item[1]
        return _line

######################

class Question():
    '''Questions are created with a style, inquiry, choices, and an answer.
    Each question has a unique ID'''

    def __init__(self, qvalues, qkeys):
        self._uid=id(self)
        self._values=[]
        self._values.append(self._uid)
        for qvalue in qvalues:
            self._values.append(qvalue)
        self._keys=[]
        for qkey in qkeys:
            self._keys.append(qkey)

    def update(self,qvalues,qkeys):
        self.__init__(qvalues,qkeys)

    def set_uid(self,_uid,_values=[]):
        '''Set the unique identifier. If a set of values are
        sent in, the unique identifier is checked against them'''
        while self.check_uid_present(_uid,_values):
            _uid+=1    
        self._uid=_uid

    def check_uid_present(self,_uid,_values=[]):
        for value in _values:
            if _uid==value:
                return True
        return False

    ##########################
    #Prompting for user input#
    ##########################

    @staticmethod
    def prompt_for_style():
        _options = Option.generate_option_list(Question_Styles.get_styles())
        _selection_message = "\nPlease select a question style\n"
        _header="\nwhat is the question style?\n"
        return Menu_Factory.run_option_menu(_options,_selection_message,_header)
        
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
        _options=Option.generate_option_list(_choices)
        _selection_message="\nSelect correct answer\n"
        _header="\nWhich choice is the correct answer?\n"
        return Menu_Factory.run_option_menu(_options,_selection_message,_header)

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
        _options=Option.generate_option_list(_choices)
        _selection_message="\nSelect correct answer"
        _header="\nWhich choice is the correct answer?\n"
        return Menu_Factory.run_option_menu(_options,_selection_message,_header)

##################
#QUESTION FACTORY#
##################

class Question_Factory():

    @staticmethod
    def create_question(qstyle):
        if qstyle == Question_Styles.true_false:
            return Question_Factory.create_true_false_question()
        elif qstyle == Question_Styles.multiple_choice:
            return Question_Factory.create_multiple_choice_question()
        elif qstyle == Question_Styles.fill_in_the_blank:
            return Question_Factory.create_fill_in_the_blank_question()

    @staticmethod
    def create_true_false_question(qvalues=[],qkeys=Question_Keys.get_keys()):
        return True_False(qvalues,qkeys)

    @staticmethod
    def create_multiple_choice_question(qvalues=[],qkeys=Question_Keys.get_keys()):
        return Multiple_Choice(qvalues,qkeys)

    @staticmethod
    def create_fill_in_the_blank_question(qvalues=[],qkeys=Question_Keys.get_keys()):
        return Fill_In_The_Blank(qvalues,qkeys)
