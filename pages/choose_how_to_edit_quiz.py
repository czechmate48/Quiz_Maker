from cache import CacheCat
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import QuestionFactory, QuestionKeys
from storage import Storage


class ChooseHowToEditQuiz(Page):

    def __init__(self, file_path):
        self._file_path = file_path  # Pass along to next page
        self._answer = ""

    def display(self):
        self.cache_questions()
        self.prompt_for_method()

    def cache_questions(self):
        question_factory = QuestionFactory()
        Storage.cache_elements_in_file(QuestionKeys.get_keys(), self._file_path,
                                       CacheCat.question, question_factory)

    def prompt_for_method(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._answer = Menu_Factory.run_option_menu_no_sm(_choices, "What would you like to do?")

    def get_options(self):
        _options = [
            PageOptions.add_question,
            PageOptions.delete_question,
            PageOptions.back,
            PageOptions.quit
        ]
        return _options

    def get_next_page(self):
        _answer = self._answer.display_value
        if _answer == PageOptions.add_question:
            return NextPage(PageOptions.add_questions_to_quiz, self._file_path)
        elif _answer == PageOptions.delete_question:
            return NextPage(PageOptions.delete_question, self._file_path)
        elif _answer == PageOptions.back:
            return NextPage(PageOptions.choose_quiz_to_edit)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
