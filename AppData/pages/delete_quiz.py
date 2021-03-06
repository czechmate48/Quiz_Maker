import os

from memory.cache import QuizCache, CacheCat
from format.menu import OptionFactory, MenuFactory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from memory.storage import Storage, StorageData


class DeleteQuiz(Page):

    """User selects a quiz to delete, quiz is deleted from quizzes.qz, .qst file is deleted"""

    def __init__(self, _quiz_file_path):
        super().__init__()
        self._select_quiz_to_delete_question = "Which quiz would you like to delete?"
        self._select_quiz_to_delete_answer = ''
        self._quiz_file_path = _quiz_file_path
        self._sure_about_deleting_question = "Are you sure you want to delete "

    #  CALLED EXTERNALLY
    def display(self):
        _choices = OptionFactory.generate_unlinked_options(self.get_options())
        self._select_quiz_to_delete_answer = \
            MenuFactory.run_option_menu_no_sm(_choices, self._select_quiz_to_delete_question)

    @staticmethod
    def get_options():
        _options = []
        _quizzes = QuizCache.get_all_values_in_cache(CacheCat.quiz)
        for quiz in _quizzes:
            _options.append(quiz.get_name())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options

    ############

    #  CALLED EXTERNALLY
    def get_next_page(self):
        _answer = self._select_quiz_to_delete_answer.display_value
        if _answer == PageOptions.back:
            return NextPage(PageOptions.home)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            _remove_quiz_answer = self.ask_if_sure_about_deleting_quiz()
            if _remove_quiz_answer:
                self.remove_quiz()
            return NextPage(PageOptions.delete_quiz, self._quiz_file_path)

    def ask_if_sure_about_deleting_quiz(self):
        _delete_quiz_question = self._sure_about_deleting_question + \
                                self._select_quiz_to_delete_answer.display_value + "? (Yes/No)"
        _delete_quiz = MenuFactory.run_yes_no_menu(_delete_quiz_question)
        if _delete_quiz == "n" or _delete_quiz == "no":
            return False
        else:
            return True

    def remove_quiz(self):
        _quizzes = QuizCache.get_all_values_in_cache(CacheCat.quiz)
        for _quiz in _quizzes:
            if self.cached_quiz_matches_selected_question(_quiz):
                self.remove_quiz_from_cache(_quiz)
                self.refresh_question_file()
                self.remove_quiz_question_file(_quiz)

    def cached_quiz_matches_selected_question(self, _quiz):
        return _quiz.get_name() == self._select_quiz_to_delete_answer.display_value

    @staticmethod
    def remove_quiz_from_cache(_quiz):
        QuizCache.remove_value_from_cache(CacheCat.quiz, _quiz)

    def refresh_question_file(self):
        os.remove(self._quiz_file_path)
        Storage.create_new_file(self._quiz_file_path)
        for _quiz in QuizCache.get_all_values_in_cache(CacheCat.quiz):
            Storage.append_element_to_file(self._quiz_file_path, _quiz.content)

    def remove_quiz_question_file(self, _quiz):
        _quiz_question_path = StorageData.data_directory_path + self._select_quiz_to_delete_answer.display_value \
                              + StorageData.question_file_extension
        os.remove(_quiz_question_path)



