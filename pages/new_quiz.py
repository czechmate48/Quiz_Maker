from dataclasses import dataclass

from cache import QuizCache, CacheCat
from menu import Menu_Factory
from pages.home import Home
from pages.page import Page, PageOptions, PageFactory, AddQuestionsToQuiz
from question import Question
from quiz import Quiz, QuizKeys
from storage import Storage


@dataclass
class NQPageOptions:
    home: str = "Home"
    add_questions_to_quiz: str = "Add Questions to Quiz"
    quit: str = "Quit"
    back: str = "Back"

    @staticmethod
    def get_page_options():
        k = PageOptions()
        return [k.__dict__[var] for var in k.__dict__]


class NQPageFactory:

    @staticmethod
    def create_page(page, _file_path=""):
        if page == NQPageOptions.home:
            return Home()
        elif page == NQPageOptions.add_questions_to_quiz:
            return AddQuestionsToQuiz(_file_path)


class NewQuiz(Page):

    """Creates a new quiz and adds it to the quiz cache"""

    def display(self):
        _quiz = self.prompt_user_for_quiz_keys()
        self.save_quiz_to_file(_quiz)
        _answer = self.prompt_to_add_questions(_quiz)
        _next_page = self.get_next_page(_answer)
        return _next_page

    @staticmethod
    def prompt_user_for_quiz_keys():
        _name = Quiz.prompt_for_name()
        _style = Quiz.prompt_for_style()
        _question_file = _name + Question.extension  # location of question file determined by config file
        _values = (_name, _style, _question_file)
        return Quiz(_values, QuizKeys.get_keys(), True)

    def save_quiz_to_file(self, _quiz):
        self.question_file_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/' + _quiz.get_name() + ".qst"
        QuizCache.add_value_to_cache(CacheCat.quiz, _quiz)
        # FIXME -> Update filepath to correct path when done testing
        _quiz_file_path = Storage.get_config_value('/data/file_paths.txt', 'quiz_file_path')
        Storage.append_element_to_file(_quiz_file_path, _quiz.content)
        Storage.create_new_file(self.question_file_path)

    def prompt_to_add_questions(self, _quiz):
        _add_questions_selection = Menu_Factory.run_yes_no_menu("\nWould you like to add questions?")
        return _add_questions_selection

    def get_next_page(self, _answer):
        _answer = _answer.lower()
        if _answer == 'n' or _answer == "no":
            return NQPageFactory.create_page(NQPageOptions.home)
        else:
            return NQPageFactory.create_page(PageOptions.add_questions_to_quiz, self.question_file_path)



