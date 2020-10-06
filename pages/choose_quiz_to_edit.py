from cache import QuizCache, CacheCat
from menu import Option_Factory, Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions


class ChooseQuizToEdit(Page):

    """Allows user to select a quiz from the available quizzes;
    Returns an edit page for a quiz's question file"""

    def __init__(self):
        self._quiz_question_path = ""
        self._answer = ""

    def display(self):
        self.prompt_for_quiz()  # May also return quit or back

    def get_next_page(self):
        _answer = self._answer.display_value
        if _answer == PageOptions.back:
            return NextPage(PageOptions.home)
        elif _answer == PageOptions.quit:
            return NextPage(PageOptions.quit)
        else:
            self._quiz_question_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/' + _answer + '.qst'
            return NextPage(PageOptions.choose_how_to_edit_quiz, self._quiz_question_path)

    def prompt_for_quiz(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        self._answer = Menu_Factory.run_option_menu_no_sm(_choices, "Which quiz would you like to edit?")

    def get_options(self):
        _options = []
        for _quiz in QuizCache.get_all_values_in_cache(CacheCat.quiz):
            _options.append(_quiz.get_name())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options
