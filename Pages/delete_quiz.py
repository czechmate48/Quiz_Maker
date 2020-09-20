from cache import CacheCat, QuizCache
from menu import Option_Factory, Menu_Factory
from page import PageFactory, PageOptions, Page


class DeleteQuiz(Page):

    def __init__(self):
        super().__init__()
        self._options = self.get_options()
        self._header = "\nWhich quiz would you like to remove?"

    def get_options(self):
        _options = []
        _quizzes = QuizCache.get_all(CacheCat.quiz)
        for quiz in _quizzes:
            _options.append(quiz.get_name())
        _options.append(PageOptions.home_screen)
        _options.append(PageOptions.quit)
        return _options

    def display(self):
        _choices = Option_Factory.generate_unlinked_options(self._options)
        _selection = Menu_Factory.run_option_menu_no_sm(_choices, self._header)
        if _selection != 'i':
            # TODO -> Add logic
            return PageFactory.create_page(PageOptions.home_screen)

