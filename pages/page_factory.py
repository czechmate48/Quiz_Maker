import sys

from pages.add_questions_to_quiz import AddQuestionsToQuiz
from pages.choose_how_to_edit_quiz import ChooseHowToEditQuiz
from pages.delete_quiz import DeleteQuiz
from pages.delete_question import DeleteQuestion
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
            return DeleteQuiz(next_page.file_path)
        elif page_name == PageOptions.add_questions_to_quiz:  # ADD QUESTIONS TO QUIZ
            return AddQuestionsToQuiz(next_page.file_path)
        elif page_name == PageOptions.select_quiz_to_edit:
            return SelectQuizToEdit()
        elif page_name == PageOptions.choose_how_to_edit_quiz:
            return ChooseHowToEditQuiz(next_page.file_path)
        elif page_name == PageOptions.delete_question:
            return DeleteQuestion(next_page.file_path)
        elif page_name == PageOptions.quit:
            return sys.exit()  # EXIT PROGRAM
