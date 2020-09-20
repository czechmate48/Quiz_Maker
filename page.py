# page.py

"""Creates navigation pages"""

from dataclasses import dataclass
from Pages.add_questions_to_quiz import AddQuestionsToQuiz
from Pages.delete_quiz import DeleteQuiz
from Pages.edit_quiz_questions import EditQuizQuestions
from Pages.home import Home
from Pages.new_quiz import NewQuiz
from Pages.select_quiz_to_edit import SelectQuizToEdit


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
