from memory.cache import QuizCache, CacheCat
from format.menu import OptionFactory, MenuFactory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from memory.storage import StorageData


class ChooseQuizToTake(Page):

    """Allows user to select a quiz from the available quizzes;
    User will start taking the quiz"""

    def __init__(self):
        super().__init__()
        self._quiz_question_question = "Which quiz would you like to take"
        self._answer = ""

    def display(self):
        self.prompt_for_quiz()  # May also return quit or back

    def prompt_for_quiz(self):
        _choices = OptionFactory.generate_unlinked_options(self.get_options())
        self._answer = MenuFactory.run_option_menu_no_sm(_choices, self._quiz_question_question)

    def get_next_page(self):
        _answer = self._answer.display_value
        if _answer == PageOptions.back:
            return NextPage(PageOptions.home)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            _quiz_question_path = StorageData.data_directory_path + _answer + StorageData.question_file_extension
            return NextPage(PageOptions.take_quiz, _quiz_question_path)

    def get_options(self):
        _options = []
        for _quiz in QuizCache.get_all_values_in_cache(CacheCat.quiz):
            _options.append(_quiz.get_name())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options
