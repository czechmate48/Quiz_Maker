# page.py

"""Creates navigation pages"""

from dataclasses import dataclass
from cache import CacheCat, QuizCache
from menu import Option_Factory, Menu_Factory
from question import Question, QuestionFactory, QuestionKeys
from quiz import QuizKeys, Quiz, QuizFactory
from storage import Storage


@dataclass
class PageOptions:
    home_screen: str = "home Screen"
    take_quiz: str = "Take a Quiz"
    new_quiz: str = "Add a Quiz"
    delete_quiz: str = "Delete a Quiz"
    select_quiz_to_edit: str = "Edit a Quiz"
    add_questions_to_quiz = "Add Questions to Quiz"
    edit_specific_quiz = "Edit Specific Quiz"
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

    """Loads the home menu. Instantiates the QuizCache"""

    def display(self):
        self.load_quiz_cache()
        _next_page = self.prompt_for_next_menu()
        return _next_page

    def load_quiz_cache(self):
        quiz_file_path = Storage.get_config_value(
            '/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'quiz_file_path')
        quiz_factory = QuizFactory()
        Storage.cache_elements_in_file(QuizKeys.get_keys(), quiz_file_path, CacheCat.quiz, quiz_factory)

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

    """Creates a new quiz and adds it to the quiz cache"""

    def display(self):
        _quiz = self.prompt_user_for_quiz_keys()
        self.save_quiz_to_file(_quiz.get)
        _answer = self.prompt_to_add_questions(_quiz)
        _next_page = self.get_next_page(_answer)
        return _next_page

    @staticmethod
    def prompt_user_for_quiz_keys():
        _name = Quiz.prompt_for_name()
        _style = Quiz.prompt_for_style()
        _question_file = _name + Question.extension  # location of question file determined by config file
        _values = (_name, _style, _question_file)
        return Quiz(_values, QuizKeys.get_keys(), True)

    def save_quiz_to_file(self, _quiz):
        self.question_file_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/data/' + _quiz.get_name() + ".qst"
        QuizCache.add(CacheCat.quiz, _quiz)
        # FIXME -> Update filepath to correct path when done testing
        _quiz_file_path = Storage.get_config_value(
            '/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'quiz_file_path')
        Storage.append_element_to_file(_quiz_file_path, _quiz.content)
        Storage.create_new_file(self.question_file_path)

    def prompt_to_add_questions(self, _quiz):
        _add_questions_selection = Menu_Factory.run_yes_no_menu("\nWould you like to add questions?")
        return _add_questions_selection

    def get_next_page(self, _answer):
        if _answer == 'no' or _answer == 'n' or _answer == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            return PageFactory.create_page(PageOptions.add_questions_to_quiz, self.question_file_path)


class AddQuestionsToQuiz(Page):

    """Allows user to add questions to a specific quiz;
    requires a path to the quiz's question file"""

    def __init__(self, _file_path):
        # TODO -> Update way of accessing file path
        self._file_path = _file_path

    def display(self):
        _question = self.prompt_for_question()
        self.save_question_to_file(_question)
        _answer = self.prompt_for_add_another_question()
        _next_page = self.get_next_page(_answer)
        return _next_page

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

    def prompt_for_add_another_question(self):
        _add_question_selection = Menu_Factory.run_yes_no_menu("\nAdd another question?")
        return _add_question_selection

    def get_next_page(self, _answer):
        if _answer == 'no' or _answer == 'n' or _answer == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            return PageFactory.create_page(PageOptions.add_questions_to_quiz, self._file_path)


class SelectQuizToEdit(Page):

    """Allows user to select a quiz from the available quizzes;
    Returns an edit page for a quiz's question file"""

    def display(self):
        _quiz = self.prompt_for_quiz()
        _quiz_question_path = '/home/czechmate/Documents/python/programs/Quiz_Maker/' + _quiz + '.qst'
        _next_page = self.get_next_page(_quiz_question_path)
        return _next_page

    def prompt_for_quiz(self):
        _choices = Option_Factory.generate_unlinked_options(self.get_options())
        _quiz = Menu_Factory.run_option_menu_no_sm(_choices, "Which quiz would you like to edit?")
        return _quiz.display_value

    def get_options(self):
        _options = []
        for _quiz in QuizCache.get_all(CacheCat.quiz):
            _options.append(_quiz.get_name())
        _options.append(PageOptions.back)
        _options.append(PageOptions.quit)
        return _options

    def get_next_page(self, _quiz_question_path):
        return PageFactory.create_page(PageOptions.edit_specific_quiz, _quiz_question_path)


class EditSpecificQuiz(Page):

    """Lists all the questions in a specific quiz"""

    def __init__(self, file_path):
        self._file_path = file_path

    def display(self):
        #  START HERE
        #  Make this class list the questions in this quiz
        #  Move each class to it's own folder.
        #  Delete the Page factory and just create each Page locally
        return PageFactory.create_page(PageOptions.home_screen)


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


class PageFactory:

    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_page(page_type, _file_path=""):  # Not all pages will need _file_path variable
        if page_type == PageOptions.home_screen:  # HOME SCREEN
            return Home()
        elif page_type == PageOptions.new_quiz:  # ADD QUIZ
            return NewQuiz()
        elif page_type == PageOptions.delete_quiz:  # REMOVE QUIZ
            return DeleteQuiz()
        elif page_type == PageOptions.add_questions_to_quiz:  # ADD QUESTIONS TO QUIZ
            return AddQuestionsToQuiz(_file_path)
        elif page_type == PageOptions.select_quiz_to_edit:
            return SelectQuizToEdit()
        elif page_type == PageOptions.edit_specific_quiz:
            return EditSpecificQuiz(_file_path)

