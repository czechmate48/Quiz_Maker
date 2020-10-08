import sys
from dataclasses import dataclass


@dataclass
class PageOptions:
    home: str = "Home"
    add_new_quiz: str = "Add a Quiz"
    add_questions_to_quiz: str = "Add Questions to Quiz"
    add_question: str = "Add Question"
    choose_quiz_to_edit: str = "Edit a Quiz"
    choose_how_to_edit_quiz: str = "Choose how to edit quiz"  # Don't list in options
    choose_quiz_to_take: str = "Take a Quiz"
    edit_specific_quiz: str = "Edit Specific Quiz"
    edit_specific_question: str = "Edit Specific Question"  # Place holder for specific question
    delete_question: str = "Delete Question"
    delete_quiz: str = "Delete a Quiz"
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
        pass
