from menu import Menu_Factory
from pages.next_page import NextPage
from pages.page import Page, PageOptions
from question import Question, QuestionFactory, QuestionKeys
from storage import Storage


class AddQuestionsToQuiz(Page):
    """Adds one or more questions to a .qst file"""

    def __init__(self, qst_file_path):
        super().__init__()
        self.qst_file_path = qst_file_path
        self.add_another_question_answer = "n"
        self.add_another_question_question = "\nAdd another question?"

    #  CALLED EXTERNALLY
    def display(self):
        _question = self.prompt_for_question()
        self.save_question_to_file(_question)
        self.add_another_question_answer = self.prompt_for_add_another_question()

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
        Storage.append_element_to_file(self.qst_file_path, _question.content)

    def prompt_for_add_another_question(self):
        _add_question_selection = Menu_Factory.run_yes_no_menu(self.add_another_question_question)
        return _add_question_selection

    ##################

    #  CALLED EXTERNALLY
    def get_next_page(self):
        _add_another_question = self.add_another_question_answer.lower()
        return self.select_page_based_on_answer(_add_another_question)

    def select_page_based_on_answer(self, _answer):
        if _answer == 'n' or _answer == "no":
            return NextPage(PageOptions.home)
        elif _answer == 'y' or _answer == "yes":
            return NextPage(PageOptions.add_questions_to_quiz, self.qst_file_path)
        else:
            self.prompt_for_add_another_question()
