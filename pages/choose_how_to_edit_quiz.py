from cache import CacheCat
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import QuestionFactory, QuestionKeys
from storage import Storage


class ChooseHowToEditQuiz(Page):
    """Cache .qst questions, allows user to select how to edit a specific quiz"""

    def __init__(self, qst_file_path):
        super().__init__()
        self._qst_file_path = qst_file_path
        self._how_to_edit_quiz_question = "How would you like to edit this quiz?"
        self._how_to_edit_quiz_answer = ""

    #  CALLED EXTERNALLY
    def display(self):
        self.cache_questions()
        self.prompt_for_method_to_edit_quiz()

    def cache_questions(self):
        question_factory = QuestionFactory()
        Storage.cache_elements_in_file(QuestionKeys.get_keys(), self._qst_file_path,
                                       CacheCat.question, question_factory)

    def prompt_for_method_to_edit_quiz(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._how_to_edit_quiz_answer = Menu_Factory.run_option_menu_no_sm(_choices, self._how_to_edit_quiz_question)

    @staticmethod
    def get_options():
        _options = [
            PageOptions.add_question,
            PageOptions.delete_question,
            PageOptions.back,
            PageOptions.quit
        ]
        return _options

    ##################

    # CALLED EXTERNALLY
    def get_next_page(self):
        _answer = self._how_to_edit_quiz_answer.display_value
        return self.select_page_based_on_answer(_answer)

    def select_page_based_on_answer(self, _answer):
        if _answer == PageOptions.add_question:
            return NextPage(PageOptions.add_questions_to_quiz, self._qst_file_path)
        elif _answer == PageOptions.delete_question:
            return NextPage(PageOptions.delete_question, self._qst_file_path)
        elif _answer == PageOptions.back:
            return NextPage(PageOptions.choose_quiz_to_edit)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
