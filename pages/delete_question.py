import os

from cache import CacheCat, QuestionCache
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import QuestionFactory, QuestionKeys
from storage import Storage


class DeleteQuestion(Page):

    """Lists all the questions in a specific quiz"""

    def __init__(self, file_path):
        self._file_path = file_path
        self._question_inquiry = ''  # Will be equal to the answer
        self._answer = ''  # Can be a specific question or back/quit

    def display(self):
        self.cache_questions()
        self.prompt_for_question()

    def get_next_page(self):
        _answer = self._answer.display_value
        if _answer == PageOptions.back:
            return NextPage(PageOptions.choose_how_to_edit_quiz, self._file_path)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            self._question_inquiry = _answer
            self.remove_question()
            print("\n" + self._question_inquiry + " removed")
            return NextPage(PageOptions.delete_question, self._file_path)

    def remove_question(self):
        _all_questions = QuestionCache.get_all_values_in_cache(CacheCat.question)
        for _question in _all_questions:
            if self.cached_question_matches_selected_question(_question):
                self.remove_question_from_cache(_question)
                self.refresh_question_file()

    def cached_question_matches_selected_question(self, _question):
        return _question.get_inquiry() == self._question_inquiry

    def remove_question_from_cache(self, _question):
        QuestionCache.remove_value_from_cache(CacheCat.question, _question)

    def refresh_question_file(self):
        os.remove(self._file_path)
        for _question in QuestionCache.get_all_values_in_cache(CacheCat.question):
            Storage.append_element_to_file(self._file_path, _question.content)

    def cache_questions(self):
        question_factory = QuestionFactory()
        Storage.cache_elements_in_file(QuestionKeys.get_keys(), self._file_path,
                                       CacheCat.question, question_factory)

    def prompt_for_question(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._answer = Menu_Factory.run_option_menu_no_sm(_choices, "Which question would you like to delete?")

    def get_options(self):
        _options = []
        for _question in QuestionCache.get_all_values_in_cache(CacheCat.question):
            _options.append(_question.get_inquiry())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options
