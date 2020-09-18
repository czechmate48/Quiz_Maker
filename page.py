# page.py

"""Creates navigation pages"""

from dataclasses import dataclass

from cache import CacheCat, QuizCache, QuestionCache
from element import Element
from menu import Menu_Factory, Option_Factory
from question import Question, QuestionFactory, QuestionKeys
from quiz import Quiz, QuizKeys
from storage import Storage


@dataclass
class PageOptions:
    home_screen: str = "Home Screen"
    take_quiz: str = "Take a Quiz"
    add_quiz: str = "Add a Quiz"
    remove_quiz: str = "Remove a Quiz"
    edit_quiz: str = "Edit a Quiz"
    add_questions_to_quiz = "Add Questions to Quiz"
    edit_specific_quiz: str = "Edit Specific Quiz"
    quit: str = "Quit"
    back: str = "Back"

    @staticmethod
    def get_page_options():
        k = PageOptions()
        return [k.__dict__[var] for var in k.__dict__]


class Page:

    def __init__(self):
        pass

    def display(self):
        pass

    def back(self):
        return Page

    def quit(self):
        pass

###############


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

#############


class AddQuiz(Page):

    def display(self):
        _name = Quiz.prompt_for_name()
        _style = Quiz.prompt_for_style()
        _question_file = _name + Question.extension  # location of question file determined by config file
        _values = (_name, _style, _question_file)
        _quiz = Quiz(_values, QuizKeys.get_keys(), True)
        self.question_file_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/' + _quiz.get_name() + ".qst"
        self.store(_quiz)
        _header = "\nWould you like to add questions?"
        _selection = Menu_Factory.run_yes_no_menu(_header)
        if _selection == 'no' or _selection == 'n' or _selection == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            return PageFactory.create_page(PageOptions.add_questions_to_quiz, self.question_file_path)

    def store(self, _quiz):
        QuizCache.add(CacheCat.quiz, _quiz)
        # FIXME -> Update filepath to correct path when done testing
        _quiz_file_path = Storage.get_config_value(
            '/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'quiz_file_path')
        Storage.append_element_to_file(_quiz_file_path, _quiz.content)
        Storage.create_new_file(self.question_file_path)

#############


class RemoveQuiz(Page):

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


class AddQuestionsToQuiz(Page):

    def __init__(self, _file_path):
        # TODO -> Update way of accessing file path
        self._file_path = _file_path

    def display(self):
        _style = Question.prompt_for_style()
        _question = QuestionFactory.create(_style)  # generate ID
        _inquiry = _question.prompt_for_inquiry()
        _choices = _question.prompt_for_choices()
        _answer = _question.prompt_for_answer(_choices)
        _question.update((_style, _inquiry, _choices, _answer), QuestionKeys.get_keys())
        # QuestionCache.add(CacheCat.question, _question)
        Storage.append_element_to_file(self._file_path, _question.content)
        _header = "\nAdd another question?"
        _selection = Menu_Factory.run_yes_no_menu(_header)
        if _selection == 'no' or _selection == 'n' or _selection == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            return PageFactory.create_page(PageOptions.add_questions_to_quiz, self._file_path)


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


class EditSpecificQuiz(Page):
    def __init__(self, quiz_name):
        self._quiz_name = quiz_name

    def get_options(self):
        _options = []
        _ #  START HERE, Add ability to see quiz questions after selecting quiz
        #  First need a screen that asks how you to edit the quiz (add question, delete, alter, etc)

    def display(self):
        _options = self.get_options()
        _choices = Option_Factory.generate_unlinked_options(_options)
        _selection = Menu_Factory.run_option_menu(_choices, self._selection_message, self._header)
        if _selection == PageOptions.edit_specific_quiz:
            return PageFactory.create_page(PageOptions.edit_specific_quiz, _selection) #  Selection will be quiz name
        else:
            return PageFactory.create_page(_selection.display_value)


class DisplayQuizQuestions(Page):


class PageFactory:

    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_page(page_type, _quiz_name=""):  # Not all pages will need quiz variable
        if page_type == PageOptions.home_screen:  # HOME SCREEN
            return Home()
        elif page_type == PageOptions.edit_quiz:  # EDIT QUIZ
            return Edit()
        elif page_type == PageOptions.add_quiz:  # ADD QUIZ
            return AddQuiz()
        elif page_type == PageOptions.remove_quiz:  # REMOVE QUIZ
            return RemoveQuiz()
        elif page_type == PageOptions.add_questions_to_quiz:  # ADD QUESTIONS TO QUIZ
            return AddQuestionsToQuiz(_quiz_name)
        elif page_type == PageOptions.edit_specific_quiz:
            return DisplayQuizQuestions(_quiz_name)
