from memory.cache import QuizCache, CacheCat
from format.menu import MenuFactory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from elements.question import Question
from elements.quiz import Quiz, QuizKeys
from memory.storage import Storage


class AddNewQuiz(Page):
    """Creates a new quiz, adds it to the quiz cache, saves it to the quizzes.qz file,
    asks if user would like to add questions to the quiz """

    def __init__(self):
        super().__init__()
        self._all_quiz_question_file_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/'
        self._new_quiz_question_file_path = ''
        self._add_questions_question = "\nWould you like to add questions? (Yes/No)"
        self._question_file_extension = ".qst"
        self._config_file_path = '../data/file_paths.txt'  # FIXME -> Update filepath to correct path when done testing
        self._quizzes_file_path = ""
        self._new_quiz = ''

    #  CALLED EXTERNALLY
    def display(self):
        self._new_quiz = self.prompt_user_for_quiz_keys()
        self.add_quiz_to_cache(self._new_quiz)
        self.save_quiz_to_file(self._new_quiz)

    @staticmethod
    def prompt_user_for_quiz_keys():
        _name = Quiz.prompt_for_name()
        _style = Quiz.prompt_for_style()
        _question_file = _name + Question.extension  # location of question file determined by config file
        _values = (_name, _style, _question_file)
        return Quiz(_values, QuizKeys.get_keys(), True)

    @staticmethod
    def add_quiz_to_cache(_quiz):
        QuizCache.add_value_to_cache(CacheCat.quiz, _quiz)

    def save_quiz_to_file(self, _quiz):
        self._new_quiz_question_file_path = self._all_quiz_question_file_path + _quiz.get_name() + self._question_file_extension
        self._quizzes_file_path = Storage.get_config_value(self._config_file_path, 'quiz_file_path')
        Storage.append_element_to_file(self._quizzes_file_path, _quiz.content)
        Storage.create_new_file(self._new_quiz_question_file_path)

    ##################

    #  CALLED EXTERNALLY
    def get_next_page(self):
        _add_questions_answer = self.prompt_to_add_questions(self._new_quiz).lower()
        _next_page = self.select_page_based_on_answer(_add_questions_answer)
        return _next_page

    def prompt_to_add_questions(self, _quiz):
        _answer = MenuFactory.run_yes_no_menu(self._add_questions_question)
        return _answer

    def select_page_based_on_answer(self, _answer):
        if _answer == 'n' or _answer == "no":
            return NextPage(PageOptions.home)
        else:
            return NextPage(PageOptions.add_questions_to_quiz, self._new_quiz_question_file_path)
