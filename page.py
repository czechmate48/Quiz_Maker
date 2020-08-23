#page.py

'''Creates navigation pages'''

from dataclasses import dataclass
from menu import Menu_Factory, Option

@dataclass
class Page_Types():

    home: str="HOME"
    edit: str="EDIT"
    none: str="NONE"

@dataclass
class Page_Options():

    take_quiz: str="Take a Quiz"
    edit_quiz: str="Edit a Quiz"
    quit: str="Quit"
    back: str="Back"

class Page():
    
    def __init__(self,options=[]):
        self._options=options

    def display():
        pass

    def back():
        return Page

    def quit(self):
        pass

class Home(Page):

    def display(self):
        self._header="Quiz Maker 1.0"
        self._selection_message="Please make a selection"
        return Menu_Factory.run_option_menu(self._options,self._selection_message,self._header)

class Edit(Page):
    
    def display(self):
        self._header="Which quiz would you like to edit?"
        self._selection_message="Please select a quiz"
        return Menu_Factory.run_option_menu(self._options,self._selection_message,self._header)

class Page_Factory():

    def __init__():
        pass

    @classmethod
    def create_page(cls,page_type,_options=[]):
        if page_type==Page_Types.home:
            _options=[Option(Page_Options.take_quiz),Option(Page_Options.edit_quiz),Option(Page_Options.quit)]
            return Home(_options)
        elif page_type==Page_Types.edit:
            _options.append(Option(Page_Options.back))
            _options.append(Option(Page_Options.quit))
            return Edit(_options)
