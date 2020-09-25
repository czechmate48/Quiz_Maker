from cache import CacheCat, QuestionCache
from menu import Option_Factory, Menu_Factory
from pages.edit_specific_question import EditSpecificQuestion
from pages.home import Home
from pages.page import Page, PageOptions
from question import QuestionFactory, QuestionKeys
from storage import Storage


class ESQPageFactory:

    @staticmethod
    def create_page(page, _file_path=""):
        if page == PageOptions.home:
            return Home()
        elif page == PageOptions.edit_specific_quiz:
            return EditSpecificQuestion(_file_path)


class EditSpecificQuiz(Page):

    """Lists all the questions in a specific quiz"""

    def __init__(self, file_path):
        self._file_path = file_path

    def display(self):
        self.cache_questions()
        _question = self.prompt_for_question()
        _next_Page = ESQPageFactory.create_page(PageOptions.edit_specific_question)
        return ESQPageFactory.create_page(PageOptions.edit_specific_question)

    def cache_questions(self):
        question_factory = QuestionFactory()
        Storage.cache_elements_in_file(QuestionKeys.get_keys(), self._file_path,
                                       CacheCat.question, question_factory)

    def prompt_for_question(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        _question = Menu_Factory.run_option_menu_no_sm(_choices, "Which question would you like to edit?")
        return _question.display_value

    def get_options(self):
        _options = []
        for _question in QuestionCache.get_all_values_in_cache(CacheCat.question):
            _options.append(_question.get_inquiry())
        _options.append(PageOptions.home)
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options
