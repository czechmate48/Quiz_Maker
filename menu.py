#menu.py
'''This file creates a menu. It allows up to 25 menu options
with the value A-Z. Each selection will need to reference a seperate
file that contains the next set of code.'''

###########################

class Menu:
    """Menu brings in a set of options and converts them
    into a dictionary - [selection variable,option]"""

    from typing import Final

    def __init__(self,options):
        '''requires an option object from Option class'''
        self.first_option: Final = 65 #Used as a constant, starting ascii 65 (A)
        self._last_option = self.first_option 
        self._option_lim: Final = 90 #Limited to 25 menu options
        self.assigned_options={} #options assigned a corresponding letter
        for option in options:
            if self._last_option < self._option_lim:
                self.assigned_options[chr(self._last_option)] = option.title
                self._last_option+=1
            else:
                #throw out of bounds error
                break
        self.initial_selection = chr(self._option_lim+1) #initial user selection used to launch loop
        self.selection_message = "\nPlease make a selection" #Can be overriden for customization

    def display_options(self):
        for option in self.assigned_options:
            print(option,')',self.assigned_options[option])
    
    def display_selection_message(self):
        print(self.selection_message)

    def get_user_input(self):
        return input().upper()

    def get_user_selection(self):
        self._selection = self.initial_selection
        while not self.check_valid_selection(self._selection):
            self._selection=input().upper()
        return self._selection

    def check_valid_selection(self,selection):
        if Selection.greater_than_one(selection):
            self.display_selection_message()
            return False
        elif not Selection.within_bounds(ord(selection),self.first_option,self._last_option):
            self.display_selection_message()
            return False
        elif not Selection.is_unicode(ord(selection)): #lower and upper unicode values
            self.display_selection_message()
            return False
        else:
            return True

    def display_header_one(self,header):
        for x in header:
            print('#',end="")
        print('\n',header)
        for x in header:
            print('#',end="")
        print('\n',end="")

    def display_header_two(self,header):
        print(header)
        
##############################

class Option():
    """This class creates an option object which contains an option title
    as well as a path to the file containing the code"""

    def __init__(self,title,filePath='C:'):
        self.title=title
        self.filePath=filePath
        
    @staticmethod
    def generate_option_list(values):
        '''brings in an iterable and returns a list of instantiated options'''
        options = [Option(value) for value in values]
        return options

##############################
class Selection():
    """Utility class that provides static methods used to make determinations
    about the user selection"""

    @staticmethod
    def greater_than_one(string):
        return len(string)>1

    @staticmethod
    def within_bounds(value,lower,upper):
        return value >= lower and value < upper

    @staticmethod
    def is_unicode(value):
        return value > 0 and value < 0x10FFF
