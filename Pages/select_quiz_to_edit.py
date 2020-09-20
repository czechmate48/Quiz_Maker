from cache import QuizCache, CacheCat
from menu import Option_Factory, Menu_Factory
from page import Page, PageOptions, PageFactory


class SelectQuizToEdit(Page):

    def __init__(self):
        super().__init__()
        self._selection_message = ""
        self._header = "Which quiz would you like to edit?"

    def get_options(self):
        _options = []
        _quizzes = QuizCache.get_all(CacheCat.quiz)
        for quiz in _quizzes:
            _options.append(quiz.get_name())
        _options.append(PageOptions.home_screen)
        _options.append(PageOptions.quit)
        return _options

    def display(self):
        _options = self.get_options()
        _choices = Option_Factory.generate_unlinked_options(_options)
        _selection = Menu_Factory.run_option_menu_no_sm(_choices, self._header)
        return PageFactory.create_page(_selection.display_value)