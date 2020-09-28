import sys

from pages.add_questions_to_quiz import AddQuestionsToQuiz
from pages.delete_quiz import DeleteQuiz
from pages.edit_specific_question import EditSpecificQuestion
from pages.edit_specific_quiz import EditSpecificQuiz
from pages.home import Home
from pages.new_quiz import NewQuiz
from pages.page import PageOptions
from pages.select_quiz_to_edit import SelectQuizToEdit


class PageFactory:

    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_page(next_page):  # requires a NextPage object
        page_name = next_page.next_page_name
        if page_name == PageOptions.home:
            return Home()
        elif page_name == PageOptions.new_quiz:
            return NewQuiz()
        elif page_name == PageOptions.delete_quiz:  # REMOVE QUIZ
            return DeleteQuiz()
        elif page_name == PageOptions.add_questions_to_quiz:  # ADD QUESTIONS TO QUIZ
            return AddQuestionsToQuiz(next_page.file_path)
        elif page_name == PageOptions.select_quiz_to_edit:
            return SelectQuizToEdit()
        elif page_name == PageOptions.edit_specific_quiz:
            return EditSpecificQuiz(next_page.file_path)
        elif page_name == PageOptions.edit_specific_question:
            return EditSpecificQuestion(next_page.question)
        elif page_name == PageOptions.quit:
            return sys.exit()  # EXIT PROGRAM
