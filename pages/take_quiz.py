from elements.question import QuestionFactory, QuestionKeys, Question, QuestionStyles
from elements.test_answer import TestAnswer, TestAnswerKeys
from format.menu import MenuFactory, OptionFactory
from memory.cache import CacheCat, QuestionCache, AnswerSheetCache
from memory.storage import Storage
from pages.next_page import NextPage
from pages.page import Page, PageOptions


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
            if _question.get_style() == QuestionStyles.fill_in_the_blank:
                print("hello")
                self.ask_fill_in_the_blank_question(_question)
            else:
                self.ask_option_question(_question)

    def ask_fill_in_the_blank_question(self, _question):
        _answer = MenuFactory.run_no_option_menu(_question.get_inquiry())
        _status = (_answer == _question.get_answer())
        self.add_test_answer_to_cache(_answer, _question, _status)


    def ask_option_question(self, _question):
        _choices = OptionFactory.generate_unlinked_options(self.get_options(_question))
        _answer = MenuFactory.run_option_menu_no_sm(_choices, _question.get_inquiry())
        _status = (_answer.display_value == _question.get_answer())  # Wrong answers = false, right answers = true
        self.add_test_answer_to_cache(_answer.display_value, _question, _status)

    @staticmethod
    def get_options(_question: Question):
        _options = []
        _choices = _question.get_choices()
        for _choice in _choices:
            _options.append(_choice)
        return _options

    def add_test_answer_to_cache(self, _answer, _question, _status):
        _test_answer_values = [_answer, _question.get_inquiry(), _question.get_answer(), _status]
        _test_answer = TestAnswer(_test_answer_values, TestAnswerKeys.get_keys(), True, _question)
        AnswerSheetCache.add_value_to_cache(CacheCat.answer_sheet, _test_answer)

    ##################

    def get_next_page(self):
        return NextPage(PageOptions.display_wrong_answers)