from menu import Menu_Factory
from pages.page import Page, PageOptions
from question import Question, QuestionFactory, QuestionKeys
from storage import Storage


class AddQuestionsToQuiz(Page):

    """Allows user to add questions to a specific quiz;
    requires a path to the quiz's question file"""

    def __init__(self, _file_path):
        # TODO -> Update way of accessing file path
        self._file_path = _file_path
        self.next_page = PageOptions.add_questions_to_quiz

    def display(self):
        _question = self.prompt_for_question()
        self.save_question_to_file(_question)
        _answer = self.prompt_for_add_another_question()
        _next_page = self.get_next_page(_answer)
        return _next_page

    @staticmethod
    def prompt_for_question():
        _style = Question.prompt_for_style()
        _question = QuestionFactory.create_element(_style)  # generate ID
        _inquiry = _question.prompt_for_inquiry()
        _choices = _question.prompt_for_choices()
        _answer = _question.prompt_for_answer(_choices)
        _question.update((_question.get_uid(), _style, _inquiry, _choices, _answer), QuestionKeys.get_keys())
        return _question

    def save_question_to_file(self, _question):
        Storage.append_element_to_file(self._file_path, _question.content)

    def prompt_for_add_another_question(self):
        _add_question_selection = Menu_Factory.run_yes_no_menu("\nAdd another question?")
        return _add_question_selection

    def get_next_page(self, _answer):
        _answer = _answer.lower()
        if _answer == 'n' or _answer == "no":
            self.next_page = PageOptions.home
        elif _answer == 'y' or _answer == "yes":
            self.next_page = PageOptions.add_questions_to_quiz(self._file_path)
        else:
            self.prompt_for_add_another_question()

