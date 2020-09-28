from cache import QuizCache, CacheCat
from menu import Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import Question
from quiz import Quiz, QuizKeys
from storage import Storage


class NewQuiz(Page):

    """Creates a new quiz and adds it to the quiz cache"""

    def __init__(self):
        self.question_file_path = ""
        self._add_questions_answer = ""  # Unknown as page starts until user makes a selection

    def display(self):
        _quiz = self.prompt_user_for_quiz_keys()
        self.save_quiz_to_file(_quiz)
        self._add_questions_answer = self.prompt_to_add_questions(_quiz)

    def get_next_page(self):
        self._add_questions_answer = self._add_questions_answer.lower()
        if self._add_questions_answer == 'n' or self._add_questions_answer == "no":
            return NextPage(PageOptions.home)
        else:
            return NextPage(PageOptions.add_questions_to_quiz, self.question_file_path)

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
        _quiz_file_path = Storage.get_config_value('../data/file_paths.txt', 'quiz_file_path')
        Storage.append_element_to_file(_quiz_file_path, _quiz.content)
        Storage.create_new_file(self.question_file_path)

    def prompt_to_add_questions(self, _quiz):
        _add_questions_selection = Menu_Factory.run_yes_no_menu("\nWould you like to add questions?")
        return _add_questions_selection
