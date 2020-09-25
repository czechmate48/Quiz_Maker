from cache import QuizCache, CacheCat
from menu import Option_Factory, Menu_Factory
from pages.page import Page, PageOptions


class SelectQuizToEdit(Page):

    """Allows user to select a quiz from the available quizzes;
    Returns an edit page for a quiz's question file"""

    def display(self):
        _quiz = self.prompt_for_quiz()
        _quiz_question_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/' + _quiz + '.qst'
        _next_page = self.get_next_page(_quiz_question_path)
        return _next_page

    def prompt_for_quiz(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        _quiz = Menu_Factory.run_option_menu_no_sm(_choices, "Which quiz would you like to edit?")
        return _quiz.display_value

    def get_options(self):
        _options = []
        for _quiz in QuizCache.get_all_values_in_cache(CacheCat.quiz):
            _options.append(_quiz.get_name())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options

    def get_next_page(self, _quiz_question_path):
        return SQTEPageFactory.create_page(PageOptions.edit_specific_quiz, _quiz_question_path)
