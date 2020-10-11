import os

from cache import CacheCat, QuestionCache
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import QuestionFactory, QuestionKeys
from storage import Storage


class DeleteQuestion(Page):

    """Caches questions, Lists all the questions in a specific quiz"""

    def __init__(self, _qst_file_path):
        super().__init__()
        self._qst_file_path = _qst_file_path
        self._which_question_to_delete_question = "Which question would you like to delete?"
        self._question_to_delete_answer = ''  # Can be a specific question or back/quit

    #  CALLED EXTERNALLY
    def display(self):
        self.cache_questions_in_qst_file()
        self.prompt_for_question_to_delete()

    def cache_questions_in_qst_file(self):
        question_factory = QuestionFactory()
        Storage.cache_elements_in_file(QuestionKeys.get_keys(), self._qst_file_path,
                                       CacheCat.question, question_factory)

    def prompt_for_question_to_delete(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._question_to_delete_answer = \
            Menu_Factory.run_option_menu_no_sm(_choices, self._which_question_to_delete_question)

    @staticmethod
    def get_options():
        _options = []
        for _question in QuestionCache.get_all_values_in_cache(CacheCat.question):
            _options.append(_question.get_inquiry())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options

    ##################

    #  CALLED EXTERNALLY
    def get_next_page(self):
        _answer = self._question_to_delete_answer.display_value
        if _answer == PageOptions.back:
            return NextPage(PageOptions.choose_how_to_edit_quiz, self._qst_file_path)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            _selected_question_inquiry = _answer
            self.remove_question(_selected_question_inquiry)
            return NextPage(PageOptions.delete_question, self._qst_file_path)

    def remove_question(self, _selected_question_inquiry):
        print("\n" + _selected_question_inquiry + " removed")
        _all_questions = QuestionCache.get_all_values_in_cache(CacheCat.question)
        for _question in _all_questions:
            if self.cached_question_matches_selected_question(_question, _selected_question_inquiry):
                self.remove_question_from_cache(_question)
                self.refresh_question_file()

    @staticmethod
    def cached_question_matches_selected_question(_question, _selected_question_inquiry):
        return _question.get_inquiry() == _selected_question_inquiry

    @staticmethod
    def remove_question_from_cache(_question):
        QuestionCache.remove_value_from_cache(CacheCat.question, _question)

    def refresh_question_file(self):
        os.remove(self._qst_file_path)
        _num_questions = len(QuestionCache.get_all_values_in_cache(CacheCat.question))
        if _num_questions == 0:
            Storage.create_new_file(self._qst_file_path)
        for _question in QuestionCache.get_all_values_in_cache(CacheCat.question):
            Storage.append_element_to_file(self._qst_file_path, _question.content)
