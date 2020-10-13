from memory.cache import QuizCache, CacheCat
from format.menu import OptionFactory, MenuFactory
from pages.next_page import NextPage
from pages.page import Page, PageOptions


class ChooseQuizToEdit(Page):
    """User selects a quiz from the available quizzes;
    Returns an edit page for a quiz's .qst file"""

    def __init__(self):
        super().__init__()
        self._quiz_question_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/'
        self._quiz_question_extension = ".qst"
        self._choose_quiz_question = "Which quiz would you like to edit?"
        self._choose_quiz_answer = ""

    #  CALLED EXTERNALLY
    def display(self):
        self.prompt_for_answer()  # May also return quit or back

    def prompt_for_answer(self):
        _choices = OptionFactory.generate_unlinked_options(self.get_options())
        self._choose_quiz_answer = MenuFactory.run_option_menu_no_sm(_choices, self._choose_quiz_question)

    @staticmethod
    def get_options():
        _options = []
        for _quiz in QuizCache.get_all_values_in_cache(CacheCat.quiz):
            _options.append(_quiz.get_name())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options

    ###############

    #  CALLED EXTERNALLY
    def get_next_page(self):
        _answer = self._choose_quiz_answer.display_value
        return self.select_page_based_on_answer(_answer)

    def select_page_based_on_answer(self, _answer):
        if _answer == PageOptions.back:
            return NextPage(PageOptions.home)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            _qst_file_path = self._quiz_question_path + _answer + self._quiz_question_extension
            return NextPage(PageOptions.choose_how_to_edit_quiz, _qst_file_path)
