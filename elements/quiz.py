# quiz.py

from dataclasses import dataclass
from elements.keys import Keys
from elements.element import Element, ElementFactory
from format.menu import MenuFactory, OptionFactory


@dataclass
class QuizStyles(Keys):
    generic: str = "generic"

    @staticmethod
    def get_styles():
        k = QuizStyles()
        return [k.__dict__[var] for var in k.__dict__]


@dataclass
class QuizKeys(Keys):
    uid: str = "uid"
    name: str = "name"
    style: str = "style"
    question_file: str = "question_file"  # the name of the file that holds questions for the quiz

    @staticmethod
    def get_keys():
        k = QuizKeys()
        return [k.__dict__[var] for var in k.__dict__]


class Quiz(Element):

    @staticmethod
    def prompt_for_style():
        _options = OptionFactory.generate_unlinked_options(QuizStyles.get_styles())
        _header = "Please select a quiz style"
        _selected_option = MenuFactory.run_option_menu_no_sm(_options, _header)
        return _selected_option.display_value

    @staticmethod
    def prompt_for_name():
        _header = "\nWhat is the name of this quiz?"
        _selected_option = MenuFactory.run_no_option_menu(_header)
        return _selected_option

    def get_name(self):
        return self.content[QuizKeys.name]


class QuizFactory(ElementFactory):

    def build_element(self, style, values=[], keys=QuizKeys.get_keys(), generate_id=True):
        QuizFactory.create_element(style, values, keys, generate_id)

    @staticmethod
    def create_element(style, values=[], keys=QuizKeys.get_keys(), generate_id=True):
        if style == QuizStyles.generic:
            return QuizFactory.create_generic_question(values, keys, generate_id)

    @staticmethod
    def create_generic_question(values=[], keys=QuizKeys.get_keys(), generate_id=True):
        return Quiz(values, keys, generate_id)
