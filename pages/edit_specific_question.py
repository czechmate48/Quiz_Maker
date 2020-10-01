import os

from cache import QuestionCache, CacheCat
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import QuestionKeys
from storage import Storage


class EditSpecificQuestion(Page):

    def __init__(self, _file_path, _question_inquiry):
        self._file_path = _file_path
        self._question_inquiry = _question_inquiry
        self._answer = ''

    def display(self):
        self.prompt_for_answer()

    def get_next_page(self):
        _answer = self._answer.display_value
        if _answer == PageOptions.edit:
            self.remove_question()
            return NextPage(PageOptions.add_questions_to_quiz, self._file_path)
        elif _answer == PageOptions.delete:
            self.remove_question()
            print("/n" + self._question_inquiry + " removed")
            return NextPage(PageOptions.edit_specific_quiz, self._file_path)

    def prompt_for_answer(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._answer = Menu_Factory.run_option_menu_no_sm(_choices, "Would you like to edit or remove the question?")

    def get_options(self):
        _options = [
            PageOptions.edit,
            PageOptions.delete,
            PageOptions.home,
            PageOptions.quit
        ]

        return _options

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
