# question.py
"""Creates a question object that contains a variable for
each component of a question. Note that the question object
does NOT produce a dictionary by default, and will need to
be converted to  a dictionary using the built in method"""

from format.menu import MenuFactory, OptionFactory, Option
from dataclasses import dataclass
from memory.storage import Storage
from elements.keys import Keys
from elements.element import Element, ElementFactory


#######################

@dataclass
class QuestionStyles(Keys):
    """This class holds the various types of styles a question can be.
    Extend class and just add values as needed for new styles"""

    generic: str = "Generic"
    true_false: str = "True/False"
    multiple_choice: str = "Multiple Choice"
    fill_in_the_blank: str = "Fill in the blank"

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
        return MenuFactory.run_option_menu_no_sm(_options, _header)


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
        _options = OptionFactory.generate_unlinked_options(QuestionStyles.get_keys())
        _selection_message = "Please select a question style"
        _selected_option = MenuFactory.run_option_menu_no_sm(_options, _selection_message)
        return _selected_option.display_value

    def prompt_for_inquiry(self):
        _header = "Please input a question"
        return MenuFactory.run_no_option_menu(_header)

    def prompt_for_choices(self):
        return []

    def prompt_for_answer(self, _choices):
        _header = "Please input the answer"
        return MenuFactory.run_no_option_menu(_header)

    def get_inquiry(self):
        return self.content[QuestionKeys.inquiry]

    def get_uid(self):
        return self.content[QuestionKeys.uid]

    def get_answer(self):
        return self.content[QuestionKeys.answer]

    def get_choices(self):
        return self.content[QuestionKeys.choices]

    def get_style(self):
        return self.content[QuestionKeys.style]

    def update(self, values, keys):
        self.content = self.merge_input(values, keys)

    def ask_inquiry(self):
        _inquiry = self.content[QuestionKeys.inquiry]
        _options = self.content[QuestionKeys.choices]
        return MenuFactory.run_option_menu()


#####################
# QUESTION CHILDREN #
#####################

class TrueFalse(Question):

    def __init__(self, values, keys, generate_id):  # generate_id auto assigned in parent
        super(TrueFalse, self).__init__(values, keys, generate_id)

    def prompt_for_choices(self):
        return ["true", "false"]

    def prompt_for_answer(self, _choices):
        _options = OptionFactory.generate_unlinked_options(_choices)
        _header = "Which choice is the correct answer?"
        _selected_option = MenuFactory.run_option_menu_no_sm(_options, _header)
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
                _header = "Please input the number of choices"
                _num_choices = MenuFactory.run_no_option_menu(_header)
                _num_choices = int(_num_choices)
            except ValueError:
                _num_choices = -1
        return _num_choices

    def get_choices_from_user(self, _num_choices):
        _choices = []
        while _num_choices > 0:
            print("\nplease input a choice")
            _choices.append(input())
            _num_choices -= 1
        return _choices

    def prompt_for_answer(self, _choices):
        _options = OptionFactory.generate_unlinked_options(_choices)
        _header = "Which choice is the correct answer?"
        _selected_option = MenuFactory.run_option_menu_no_sm(_options, _header)
        return _selected_option.display_value


####################
# QUESTION FACTORY #
####################

class QuestionFactory(ElementFactory):

    def build_element(self, style, values=[], keys=QuestionKeys.get_keys(), generate_id=True):
        QuestionFactory.create_element(style, values, keys, generate_id)

    @staticmethod
    def create_element(style, values=[], keys=QuestionKeys.get_keys(), generate_id=True):
        if style == QuestionStyles.true_false:
            return QuestionFactory.create_true_false_question(values, keys, generate_id)
        elif style == QuestionStyles.multiple_choice:
            return QuestionFactory.create_multiple_choice_question(values, keys, generate_id)
        elif style == QuestionStyles.fill_in_the_blank:
            return QuestionFactory.create_fill_in_the_blank_question(values, keys, generate_id)
        else:
            return QuestionFactory.create_generic_question(values, keys, generate_id)

    @staticmethod
    def create_true_false_question(values=[], keys=QuestionKeys.get_keys(), generate_id=True):
        return TrueFalse(values, keys, generate_id)

    @staticmethod
    def create_multiple_choice_question(values=[], keys=QuestionKeys.get_keys(), generate_id=True):
        return MultipleChoice(values, keys, generate_id)

    @staticmethod
    def create_fill_in_the_blank_question(values=[], keys=QuestionKeys.get_keys(), generate_id=True):
        return FillInTheBlank(values, keys, generate_id)

    @staticmethod
    def create_generic_question(values=[], keys=QuestionKeys.get_keys(), generate_id=True):
        return Question(values, keys, generate_id)
