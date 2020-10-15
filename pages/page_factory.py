import sys

from pages.add_questions_to_quiz import AddQuestionsToQuiz
from pages.choose_how_to_edit_quiz import ChooseHowToEditQuiz
from pages.choose_quiz_to_take import ChooseQuizToTake
from pages.delete_quiz import DeleteQuiz
from pages.delete_question import DeleteQuestion
from pages.home import Home
from pages.add_new_quiz import AddNewQuiz
from pages.page import PageOptions
from pages.choose_quiz_to_edit import ChooseQuizToEdit
from pages.take_quiz import TakeQuiz


class PageFactory:

    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_page(next_page):  # requires a NextPage object
        page_name = next_page.next_page_name
        if page_name == PageOptions.home:
            return Home()
        elif page_name == PageOptions.add_new_quiz:
            return AddNewQuiz()
        elif page_name == PageOptions.delete_quiz:  # REMOVE QUIZ
            return DeleteQuiz(next_page.file_path)
        elif page_name == PageOptions.add_questions_to_quiz:  # ADD QUESTIONS TO QUIZ
            return AddQuestionsToQuiz(next_page.file_path)
        elif page_name == PageOptions.choose_quiz_to_edit:
            return ChooseQuizToEdit()
        elif page_name == PageOptions.choose_how_to_edit_quiz:
            return ChooseHowToEditQuiz(next_page.file_path)
        elif page_name == PageOptions.delete_question:
            return DeleteQuestion(next_page.file_path)
        elif page_name == PageOptions.choose_quiz_to_take:
            return ChooseQuizToTake()
        elif page_name == PageOptions.take_quiz:
            return TakeQuiz(next_page.file_path)
        elif page_name == PageOptions.quit:
            return sys.exit()  # EXIT PROGRAM
