from menu import Option_Factory, Menu_Factory
from page import Page, PageOptions, PageFactory


class EditQuizQuestions(Page):
    def __init__(self, quiz_name):
        self._quiz_name = quiz_name

    def get_options(self):
        _options = []
        #  START HERE, Add ability to see quiz questions after selecting quiz
        #  First need a screen that asks how you to edit the quiz (add question, delete, alter, etc)

    def display(self):
        _options = self.get_options()
        _choices = Option_Factory.generate_unlinked_options(_options)
        _selection = Menu_Factory.run_option_menu(_choices, self._selection_message, self._header)
        if _selection == PageOptions.edit_specific_quiz:
            return PageFactory.create_page(PageOptions.edit_specific_quiz, _selection) #  Selection will be quiz name
        else:
            return PageFactory.create_page(_selection.display_value)

