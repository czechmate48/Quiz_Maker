#page.py

'''Creates navigation pages'''

from dataclasses import dataclass
from menu import Menu_Factory, Option, Option_Factory
from quiz import Quiz

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
    
    def __init__(self):
        pass

    def display(self):
        pass

    def back():
        return Page

    def quit(self):
        pass

class Home(Page):

    def get_options(self):
        _options=[]
        _options.append(Page_Options.add_quiz)
        _options.append(Page_Options.remove_quiz)
        _options.append(Page_Options.edit_quiz)
        _options.append(Page_Options.take_quiz)
        _options.append(Page_Options.quit)
        return _options

    def display(self):
        self._header="Quiz Maker 1.0"
        self._selection_message="Please make a selection"
        _options=self.get_options()
        _choices=Option_Factory.generate_unlinked_options(_options)
        _selection=Menu_Factory.run_option_menu(_choices,self._selection_message,self._header)
        return Page_Factory.create_page(_selection.display_value) 

class Add_Quiz(Page):

    def display(self):
        _name=Quiz.prompt_for_name()
        _style=Quiz.prompt_for_style()
        #Add to quiz cache
        _header="\nWould you like to add questions?"
        _selection=Menu_Factory.run_yes_no_menu(_header)
        if _selection=='no' or _selection=='n':
            return Page_Factory.create_page(Page_Options.home_screen)
        else:
            return Page_Factory.create_page(Page_Options.edit_quiz)

class Edit(Page):

    def get_options(self):
        _options=[]
        _options.append(Page_Options.home_screen)
        _options.append(Page_Options.quit)
        return _options

    def display(self):
        self._header="Which quiz would you like to edit?"
        self._selection_message=""
        #_quizes=Quiz_Cache.get_all(Cache_Cat.quiz)
        _options=self.get_options()
        _choices=Option_Factory.generate_unlinked_options(_options)
        _selection=Menu_Factory.run_option_menu_no_sm(_choices,self._header)
        return Page_Factory.create_page(_selection.display_value)

class Page_Factory():

    def __init__():
        pass

    @staticmethod
    def create_page(page_type,):
        if page_type==Page_Options.home_screen: #HOME SCREEN
            return Home()
        elif page_type==Page_Options.edit_quiz: #EDIT QUIZ
            return Edit()
        elif page_type==Page_Options.add_quiz: #ADD QUIZ
            return Add_Quiz()
