# page.py

"""Creates navigation pages"""

from dataclasses import dataclass
from menu import Menu_Factory, Option, Option_Factory
from quiz import Quiz, QuizKeys
from cache import CacheCat, QuizCache, QuestionCache
from question import Question


@dataclass
class PageOptions:
    home_screen: str = "Home Screen"
    take_quiz: str = "Take a Quiz"
    add_quiz: str = "Add a Quiz"
    remove_quiz: str = "Remove a Quiz"
    edit_quiz: str = "Edit a Quiz"
    quit: str = "Quit"
    back: str = "Back"


class Page:

    def __init__(self):
        pass

    def display(self):
        pass

    def back(self):
        return Page

    def quit(self):
        pass


class Home(Page):

    def __init__(self):
        super().__init__()
        self._selection_message = "Please make a selection"
        self._header = "Quiz Maker 1.0"

    def get_options(self):
        _options = [
            PageOptions.add_quiz,
            PageOptions.remove_quiz,
            PageOptions.edit_quiz,
            PageOptions.take_quiz,
            PageOptions.quit
        ]
        return _options

    def display(self):
        _options = self.get_options()
        _choices = Option_Factory.generate_unlinked_options(_options)
        _selection = Menu_Factory.run_option_menu(_choices, self._selection_message, self._header)
        return PageFactory.create_page(_selection.display_value)


class AddQuiz(Page):

    def display(self):
        _name = Quiz.prompt_for_name()
        _style = Quiz.prompt_for_style()
        _question_file = _name + Question.extension  # location of question file determined by config file
        _values = (_name, _style, _question_file)
        _quiz = Quiz(_values, QuizKeys.get_keys(), True)
        QuizCache.add(CacheCat.quiz, _quiz)
        _header = "\nWould you like to add questions?"
        _selection = Menu_Factory.run_yes_no_menu(_header)
        if _selection == 'no' or _selection == 'n' or _selection == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            # TODO -> Add logic
            return PageFactory.create_page(PageOptions.edit_quiz)


class Remove_Quiz(Page):

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


class Edit(Page):

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


class PageFactory:

    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_page(page_type):
        if page_type == PageOptions.home_screen:  # HOME SCREEN
            return Home()
        elif page_type == PageOptions.edit_quiz:  # EDIT QUIZ
            return Edit()
        elif page_type == PageOptions.add_quiz:  # ADD QUIZ
            return AddQuiz()
        elif page_type == PageOptions.remove_quiz:  # REMOVE QUIZ
            return Remove_Quiz()
