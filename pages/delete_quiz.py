import os

from cache import QuizCache, CacheCat
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from storage import Storage


class DeleteQuiz(Page):

    def __init__(self, _file_path):
        super().__init__()
        self._answer = ''
        self._file_path = _file_path

    def display(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._answer = Menu_Factory.run_option_menu_no_sm(_choices, "\nWhich quiz would you like to delete?")

    def get_options(self):
        _options = []
        _quizzes = QuizCache.get_all_values_in_cache(CacheCat.quiz)
        for quiz in _quizzes:
            _options.append(quiz.get_name())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options

    def get_next_page(self):
        _answer = self._answer.display_value
        if _answer == PageOptions.back:
            return NextPage(PageOptions.home)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            self.remove_quiz()
            return NextPage(PageOptions.delete_quiz, self._file_path)

    def remove_quiz(self):
        _quizzes = QuizCache.get_all_values_in_cache(CacheCat.quiz)
        for _quiz in _quizzes:
            if self.cached_quiz_matches_selected_question(_quiz):
                self.remove_quiz_from_cache(_quiz)
                self.refresh_question_file()
                self.remove_quiz_question_file(_quiz)

    def cached_quiz_matches_selected_question(self, _quiz):
        return _quiz.get_name() == self._answer.display_value

    def remove_quiz_from_cache(self, _quiz):
        QuizCache.remove_value_from_cache(CacheCat.quiz, _quiz)

    def refresh_question_file(self):
        os.remove(self._file_path)
        Storage.create_new_file(self._file_path)
        for _quiz in QuizCache.get_all_values_in_cache(CacheCat.quiz):
            Storage.append_element_to_file(self._file_path, _quiz.content)

    def remove_quiz_question_file(self, _quiz):
        _quiz_question_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/' + \
                              self._answer.display_value + '.qst'
        os.remove(_quiz_question_path)



