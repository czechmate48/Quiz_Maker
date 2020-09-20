from menu import Menu_Factory
from page import Page, PageFactory, PageOptions
from question import Question, QuestionFactory, QuestionKeys
from storage import Storage


class AddQuestionsToQuiz(Page):

    def __init__(self, _file_path):
        # TODO -> Update way of accessing file path
        self._file_path = _file_path

    def display(self):
        _style = Question.prompt_for_style()
        _question = QuestionFactory.create(_style)  # generate ID
        _inquiry = _question.prompt_for_inquiry()
        _choices = _question.prompt_for_choices()
        _answer = _question.prompt_for_answer(_choices)
        _question.update((_style, _inquiry, _choices, _answer), QuestionKeys.get_keys())
        # QuestionCache.add(CacheCat.question, _question)
        Storage.append_element_to_file(self._file_path, _question.content)
        _header = "\nAdd another question?"
        _selection = Menu_Factory.run_yes_no_menu(_header)
        if _selection == 'no' or _selection == 'n' or _selection == 'N':
            return PageFactory.create_page(PageOptions.home_screen)
        else:
            return PageFactory.create_page(PageOptions.add_questions_to_quiz, self._file_path)
