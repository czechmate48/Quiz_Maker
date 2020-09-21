# page.py

"""Creates navigation pages"""

from dataclasses import dataclass
from cache import CacheCat, QuizCache
from menu import Option_Factory, Menu_Factory
from question import Question, QuestionFactory, QuestionKeys
from quiz import QuizKeys, Quiz
from storage import Storage


@dataclass
class PageOptions:
    home_screen: str = "home Screen"
    take_quiz: str = "Take a Quiz"
    new_quiz: str = "Add a Quiz"
    delete_quiz: str = "Delete a Quiz"
    select_quiz_to_edit: str = "Edit a Quiz"
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


class Home(Page):

    def display(self):
        return self.prompt_for_next_menu()

    def prompt_for_next_menu(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_menu_options())
        _next_page = Menu_Factory.run_option_menu(_choices, "Please make a selection", "Quiz Maker 1.0")
        return PageFactory.create_page(_next_page.display_value)

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


class NewQuiz(Page):

    def display(self):
        _quiz = self.prompt_user_for_quiz_keys()
        self.save_quiz_to_file(_quiz)
        self.prompt_to_add_questions(_quiz)

    @staticmethod
    def prompt_user_for_quiz_keys():
        _name = Quiz.prompt_for_name()
        _style = Quiz.prompt_for_style()
        _question_file = _name + Question.extension  # location of question file determined by config file
        _values = (_name, _style, _question_file)
        return Quiz(_values, QuizKeys.get_keys(), True)

    def save_quiz_to_file(self, _quiz):
        QuizCache.add(CacheCat.quiz, _quiz)
        # FIXME -> Update filepath to correct path when done testing
        _quiz_file_path = Storage.get_config_value(
            '/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'quiz_file_path')
        Storage.append_element_to_file(_quiz_file_path, _quiz.content)
        Storage.create_new_file(self.question_file_path)

    @staticmethod
    def prompt_to_add_questions(_quiz):
        _add_questions_selection = Menu_Factory.run_yes_no_menu("\nWould you like to add questions?")
        if _add_questions_selection == 'no' or _add_questions_selection == 'n' or _add_questions_selection == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            _question_file_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/' + _quiz.get_name() + ".qst"
            return PageFactory.create_page(PageOptions.add_questions_to_quiz, _question_file_path)


class EditQuizQuestions(Page):

    def __init__(self, quiz_name):
        self._quiz_name = quiz_name

    def get_options(self):
        _options = []
        #  START HERE, Add ability to see quiz questions after selecting quiz
        #  First need a screen that asks how you to edit the quiz (add question, delete, alter, etc)

    def display(self):
        _options = self.get_options()
        _choices = Option_Factory.generate_unlinked_options(_options)
        _selection = Menu_Factory.run_option_menu(_choices, self._selection_message, self._header)
        if _selection == PageOptions.edit_specific_quiz:
            return PageFactory.create_page(PageOptions.edit_specific_quiz, _selection) #  Selection will be quiz name
        else:
            return PageFactory.create_page(_selection.display_value)


class AddQuestionsToQuiz(Page):

    def __init__(self, _file_path):
        # TODO -> Update way of accessing file path
        self._file_path = _file_path

    def display(self):
        _question = self.prompt_for_question()
        self.save_question_to_file(_question)
        self.prompt_for_next_menu()

    @staticmethod
    def prompt_for_question():
        _style = Question.prompt_for_style()
        _question = QuestionFactory.create(_style)  # generate ID
        _inquiry = _question.prompt_for_inquiry()
        _choices = _question.prompt_for_choices()
        _answer = _question.prompt_for_answer(_choices)
        _question.update((_style, _inquiry, _choices, _answer), QuestionKeys.get_keys())
        return _question

    def save_question_to_file(self, _question):
        Storage.append_element_to_file(self._file_path, _question.content)

    def prompt_for_next_menu(self):
        _add_question_selection = Menu_Factory.run_yes_no_menu("\nAdd another question?")
        if _add_question_selection == 'no' or _add_question_selection == 'n' or _add_question_selection == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            return PageFactory.create_page(PageOptions.add_questions_to_quiz, self._file_path)


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


class SelectQuizToEdit(object):
    pass


class PageFactory:

    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_page(page_type, _quiz_name=""):  # Not all pages will need quiz variable
        if page_type == PageOptions.home_screen:  # HOME SCREEN
            return Home()
        elif page_type == PageOptions.select_quiz_to_edit:  # EDIT QUIZ
            return SelectQuizToEdit()
        elif page_type == PageOptions.new_quiz:  # ADD QUIZ
            return NewQuiz()
        elif page_type == PageOptions.delete_quiz:  # REMOVE QUIZ
            return DeleteQuiz()
        elif page_type == PageOptions.add_questions_to_quiz:  # ADD QUESTIONS TO QUIZ
            return AddQuestionsToQuiz(_quiz_name)
        elif page_type == PageOptions.edit_specific_quiz:
            return EditQuizQuestions(_quiz_name)

