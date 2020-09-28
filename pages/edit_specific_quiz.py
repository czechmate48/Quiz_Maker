from cache import CacheCat, QuestionCache
from menu import Option_Factory, Menu_Factory
from pages.edit_specific_question import EditSpecificQuestion
from pages.home import Home
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import QuestionFactory, QuestionKeys
from storage import Storage


class EditSpecificQuiz(Page):

    """Lists all the questions in a specific quiz"""

    def __init__(self, file_path):
        self._file_path = file_path
        self._answer = ''  # Can be a specific question or back/quit

    def display(self):
        self.cache_questions()
        self.prompt_for_question()

    def get_next_page(self):
        _answer = self._answer.display_value
        if _answer == PageOptions.home:
            return NextPage(PageOptions.home)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            return NextPage(PageOptions.edit_specific_question, '', _answer)  #_answer = question

    def cache_questions(self):
        question_factory = QuestionFactory()
        Storage.cache_elements_in_file(QuestionKeys.get_keys(), self._file_path,
                                       CacheCat.question, question_factory)

    def prompt_for_question(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._answer = Menu_Factory.run_option_menu_no_sm(_choices, "Which question would you like to edit?")

    def get_options(self):
        _options = []
        for _question in QuestionCache.get_all_values_in_cache(CacheCat.question):
            _options.append(_question.get_inquiry())
        _options.append(PageOptions.home)
        _options.append(PageOptions.quit)
        return _options
