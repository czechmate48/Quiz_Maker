from cache import CacheCat
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from quiz import QuizFactory, QuizKeys
from storage import Storage


class Home(Page):

    """Loads the home menu. Instantiates the QuizCache"""

    def __init__(self):
        self.next_page = PageOptions.home
        self.quiz_file_path = ''

    def display(self):
        self.load_quiz_cache()
        self.prompt_for_next_page()

    def get_next_page(self):
        _next_page = self.next_page.display_value
        if _next_page == PageOptions.delete_quiz:
            return NextPage(_next_page, self.quiz_file_path)
        else:
            return NextPage(_next_page)

    def load_quiz_cache(self):
        self.quiz_file_path = Storage.get_config_value(
            '/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'quiz_file_path')
        quiz_factory = QuizFactory()
        Storage.cache_elements_in_file(QuizKeys.get_keys(), self.quiz_file_path, CacheCat.quiz, quiz_factory)

    def prompt_for_next_page(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_menu_options())
        self.next_page = Menu_Factory.run_option_menu_no_sm(_choices, "Quiz Maker 1.0")

    @staticmethod
    def get_menu_options():
        _options = [
            PageOptions.add_new_quiz,
            PageOptions.delete_quiz,
            PageOptions.choose_quiz_to_edit,
            PageOptions.choose_quiz_to_take,
            PageOptions.quit
        ]
        return _options

