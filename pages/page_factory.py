from pages.add_questions_to_quiz import AddQuestionsToQuiz
from pages.delete_quiz import DeleteQuiz
from pages.edit_specific_question import EditSpecificQuestion
from pages.edit_specific_quiz import EditSpecificQuiz
from pages.page import PageOptions
from pages.select_quiz_to_edit import SelectQuizToEdit


class PageFactory:

    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def create_page(page_type, _file_path="", _question=''):  # Not all pages will need _file_path or _quest
        if page_type == PageOptions.delete_quiz:  # REMOVE QUIZ
            return DeleteQuiz()
        elif page_type == PageOptions.add_questions_to_quiz:  # ADD QUESTIONS TO QUIZ
            return AddQuestionsToQuiz(_file_path)
        elif page_type == PageOptions.select_quiz_to_edit:
            return SelectQuizToEdit()
        elif page_type == PageOptions.edit_specific_quiz:
            return EditSpecificQuiz(_file_path)
        elif page_type == PageOptions.edit_specific_question:
            return EditSpecificQuestion(_question)