# question.py
'''Creates a question object that contains a variable for
each component of a question. Note that the question object
does NOT produce a dictionary by default, and will need to 
be converted to  a dictionary using the built in method'''

from menu import Menu_Factory, Option_Factory, Option
from dataclasses import dataclass
from file_manager import FileWriter, FileReader
from storage import Storage
from cache import UniqueId, CacheCat, QuestionCache
from keys import Keys
from element import Element, ElementFactory
import ast


#######################

@dataclass
class QuestionStyles(Keys):
    """This class holds the various types of styles a question can be.
    Extend class and just add values as needed for new styles"""

    generic: str = "GENERIC"
    true_false: str = "TRUE/FALSE"
    multiple_choice: str = "MULTIPLE CHOICE"
    fill_in_the_blank: str = "FILL IN THE BLANK"

    @staticmethod
    def get_keys():
        k = QuestionStyles()
        return [k.__dict__[var] for var in k.__dict__]


@dataclass
class QuestionKeys(Keys):
    """This class holds the standard keys used when creating questions.
    Extend class and just add values as needed for new keys"""

    uid: str = "uid"
    style: str = "style"
    inquiry: str = "inquiry"
    choices: str = "choices"
    answer: str = "answer"

    @staticmethod
    def get_keys():
        k = QuestionKeys()
        return [k.__dict__[var] for var in k.__dict__]


class QuestionIO(Storage):

    @classmethod
    def prompt_remove_question(cls, _file_path):
        _questions = cls.get_values(QuestionKeys.inquiry, _file_path)
        _options = Option.generate_value_options(_questions)
        _header = "\nWhich question would you like to delete?\n"
        _selection_message = "\nPlease select a question\n"
        return Menu_Factory.run_option_menu(_options, _selection_message, _header)


#####################

class Question(Element):
    """Questions are created with a style, inquiry, choices, and an answer.
    Each question has a unique ID that may or may not be created at instantiation,
    depending upon whether the contents passed into the Question already have an ID"""

    extension = ".qst"  # file extension

    def __init__(self, values, keys, generate_id):  # generate_id auto assigned in parent
        super(Question, self).__init__(values, keys, generate_id)

    @staticmethod
    def prompt_for_style():
        _options = Option_Factory.generate_unlinked_options(QuestionStyles.get_keys())
        _selection_message = "\nPlease select a question style\n"
        _header = "\nwhat is the question style?\n"
        _selected_option = Menu_Factory.run_option_menu(_options, _selection_message, _header)
        return _selected_option.display_value

    def prompt_for_inquiry(self):
        _header = "Please input a question"
        return Menu_Factory.run_no_option_menu(_header)

    def prompt_for_choices(self):
        return []

    def prompt_for_answer(self, _choices):
        _header = "Please input the answer"
        return Menu_Factory.run_no_option_menu(_header)

    def get_inquiry(self):
        return self.content[QuestionKeys.inquiry]

    def get_uid(self):
        return self.content[QuestionKeys.uid]

    def update(self, values, keys):
        self.content = self.merge_input(values, keys)


###################
# QUESTION CHILDREN#
###################

class True_False(Question):

    def __init__(self, values, keys, generate_id):  # generate_id auto assigned in parent
        super(True_False, self).__init__(values, keys, generate_id)

    def prompt_for_choices(self):
        return ["true", "false"]

    def prompt_for_answer(self, _choices):
        _options = Option_Factory.generate_unlinked_options(_choices)
        _selection_message = "\nSelect correct answer\n"
        _header = "\nWhich choice is the correct answer?\n"
        _selected_option = Menu_Factory.run_option_menu(_options, _selection_message, _header)
        return _selected_option.display_value


class FillInTheBlank(Question):

    def __init__(self, values, keys, generate_id):  # generate_id auto assigned in parent
        super(FillInTheBlank, self).__init__(values, keys, generate_id)


class MultipleChoice(Question):

    def __init__(self, values, keys, generate_id=True):
        super(MultipleChoice, self).__init__(values, keys, generate_id)

    def prompt_for_choices(self):
        _num_choices = self.get_num_choices()
        return self.get_choices_from_user(_num_choices)

    def get_num_choices(self):
        _num_choices = -1
        while _num_choices == -1:
            try:
                _header = "Please  input the number of choices"
                _num_choices = Menu_Factory.run_no_option_menu(_header)
                _num_choices = int(_num_choices)
            except ValueError:
                _num_choices = -1
        return _num_choices

    def get_choices_from_user(self, _num_choices):
        _choices = []
        while _num_choices > 0:
            print("please input a choice")
            _choices.append(input())
            _num_choices -= 1
        return _choices

    def prompt_for_answer(self, _choices):
        _options = Option_Factory.generate_unlinked_options(_choices)
        _selection_message = "\nSelect correct answer"
        _header = "\nWhich choice is the correct answer?\n"
        _selected_option = Menu_Factory.run_option_menu(_options, _selection_message, _header)
        return _selected_option.display_value


####################
# QUESTION FACTORY #
####################

class QuestionFactory(ElementFactory):

    def build(self, qstyle, qvalues=[], qkeys=QuestionKeys.get_keys(), generate_id=True):
        QuestionFactory.create(qstyle, qvalues, qkeys, generate_id)

    @staticmethod
    def create(qstyle, qvalues=[], qkeys=QuestionKeys.get_keys(), generate_id=True):
        if qstyle == QuestionStyles.true_false:
            return QuestionFactory.create_true_false_question(qvalues, qkeys, generate_id)
        elif qstyle == QuestionStyles.multiple_choice:
            return QuestionFactory.create_multiple_choice_question(qvalues, qkeys, generate_id)
        elif qstyle == QuestionStyles.fill_in_the_blank:
            return QuestionFactory.create_fill_in_the_blank_question(qvalues, qkeys, generate_id)
        else:
            return QuestionFactory.create_generic_question(qvalues, qkeys, generate_id)

    @staticmethod
    def create_true_false_question(qvalues=[], qkeys=QuestionKeys.get_keys(), generate_id=True):
        return True_False(qvalues, qkeys, generate_id)

    @staticmethod
    def create_multiple_choice_question(qvalues=[], qkeys=QuestionKeys.get_keys(), generate_id=True):
        return MultipleChoice(qvalues, qkeys, generate_id)

    @staticmethod
    def create_fill_in_the_blank_question(qvalues=[], qkeys=QuestionKeys.get_keys(), generate_id=True):
        return FillInTheBlank(qvalues, qkeys, generate_id)

    @staticmethod
    def create_generic_question(qvalues=[], qkeys=QuestionKeys.get_keys(), generate_id=True):
        return Question(qvalues, qkeys, generate_id)
