#page.py

'''Creates navigation pages'''

from dataclasses import dataclass
from menu import Menu_Factory, Option, Option_Factory

@dataclass
class Page_Options():

    home_screen: str="Home Screen"
    take_quiz: str="Take a Quiz"
    add_quiz: str="Add a Quiz"
    remove_quiz: str="Delete a Quiz"
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
        _selection=Menu_Factory.run_option_menu(self._options,self._selection_message,self._header)
        return Page_Factory(_selection.display_value) 

class Edit(Page):
    
    def display(self):
        self._header="Which quiz would you like to edit?"
        self._selection_message=""
        _selection=Menu_Factory.run_option_menu_no_sm(self._options,self._header)
        return Page_Factory(_selection.display_value)

class Page_Factory():

    def __init__():
        pass

    @classmethod
    def create_page(cls,page_type,_options=[]):
        if page_type==Page_Options.home_screen: #HOME SCREEN
            _options.append(Page_Options.add_quiz)
            _options.append(Page_Options.remove_quiz)
            _options.append(Page_Options.edit_quiz)
            _options.append(Page_Options.take_quiz)
            _options.append(Page_Options.quit)
            return Home(Option_Factory.generate_unlinked_options(_options))
        elif page_type==Page_Options.edit_quiz: #EDIT QUIZ
            _quizes=Quiz_Cache.get_all(Cache_Cat.quiz)

            _options.append(Page_Options.home_screen)
            _options.append(Page_Options.quit)
            return Edit(_options)
