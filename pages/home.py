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

    def display(self):
        self.load_quiz_cache()
        self.prompt_for_next_page()

    def get_next_page(self):
        return NextPage(self.next_page.display_value)

    def load_quiz_cache(self):
        quiz_file_path = Storage.get_config_value(
            '/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'quiz_file_path')
        quiz_factory = QuizFactory()
        Storage.cache_elements_in_file(QuizKeys.get_keys(), quiz_file_path, CacheCat.quiz, quiz_factory)

    def prompt_for_next_page(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_menu_options())
        self.next_page = Menu_Factory.run_option_menu(_choices, "Please make a selection", "Quiz Maker 1.0")

    @staticmethod
    def get_menu_options():
        _options = [
            PageOptions.new_quiz,
            PageOptions.delete_quiz,
            PageOptions.select_quiz_to_edit,
            PageOptions.take_quiz,
            PageOptions.quit
        ]
        return _options

