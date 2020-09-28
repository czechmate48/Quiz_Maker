import sys
from dataclasses import dataclass


@dataclass
class PageOptions:
    home: str = "Home"
    new_quiz: str = "Add a Quiz"
    add_questions_to_quiz: str = "Add Questions to Quiz"
    select_quiz_to_edit: str = "Edit a Quiz"
    edit_specific_quiz: str = "Edit Specific Quiz"
    edit_specific_question: str = "Edit Specific Question"  # Place holder for specific question
    quit: str = "Quit"
    back: str = "Back"
    take_quiz: str = "Take a Quiz"
    delete_quiz: str = "Delete a Quiz"

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
