from elements.question import QuestionFactory, QuestionKeys, Question
from format.menu import MenuFactory, OptionFactory
from memory.cache import CacheCat, QuestionCache
from memory.storage import Storage
from pages.page import Page


class TakeQuiz(Page):

    def __init__(self, _qst_file_path):
        self._qst_file_path = _qst_file_path

    def display(self):
        self.cache_questions_in_qst_file()
        self.randomize_questions()
        self.ask_questions()

    def cache_questions_in_qst_file(self):
        question_factory = QuestionFactory()
        Storage.cache_elements_in_file(QuestionKeys.get_keys(), self._qst_file_path,
                                       CacheCat.question, question_factory)

    def randomize_questions(self):
        QuestionCache.randomize(CacheCat.question)

    def ask_questions(self):
        _question: Question
        for _question in QuestionCache.get_all_values_in_cache(CacheCat.question):
            _choices = OptionFactory.generate_unlinked_options(self.get_options(_question))
            _answer = MenuFactory.run_option_menu_no_sm(_choices, _question.get_inquiry())

    @staticmethod
    def get_options(_question: Question):
        _options = []
        _choices = _question.get_choices()
        for _choice in _choices:
            _options.append(_choice)
        return _options
