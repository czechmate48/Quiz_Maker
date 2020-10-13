from memory.cache import CacheCat
from format.menu import OptionFactory, MenuFactory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from elements.quiz import QuizFactory, QuizKeys
from memory.storage import Storage


class Home(Page):

    """Loads the home menu. Instantiates the QuizCache"""

    def __init__(self):
        self.next_page = PageOptions.home
        self._config_file_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt'
        self._config_file_name = 'quiz_file_path'
        self.quiz_file_path = ''

    #  CALLED EXTERNALLY
    def display(self):
        self.load_quiz_cache()
        self.prompt_for_next_page()

    def load_quiz_cache(self):
        self.quiz_file_path = Storage.get_config_value(self._config_file_path, self._config_file_name)
        quiz_factory = QuizFactory()
        Storage.cache_elements_in_file(QuizKeys.get_keys(), self.quiz_file_path, CacheCat.quiz, quiz_factory)

    def prompt_for_next_page(self):
        _choices = OptionFactory.generate_unlinked_options(self.get_menu_options())
        self.next_page = MenuFactory.run_option_menu_no_sm(_choices, "Quiz Maker 1.0")

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

    ##################

    #  CALLED EXTERNALLY
    def get_next_page(self):
        _next_page = self.next_page.display_value
        if _next_page == PageOptions.delete_quiz:
            return NextPage(_next_page, self.quiz_file_path)
        else:
            return NextPage(_next_page)
