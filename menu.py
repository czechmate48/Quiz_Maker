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
        self._firstOption: Final = 65 #Used as a constant, starting ascii 65 (A)
        self._lastOption = self._firstOption 
        self.optionLim: Final = 90 #Limited to 25 menu options
        self.assignedOptions={} #options assigned a corresponding letter
        for option in options:
            if self._lastOption < self.optionLim:
                self.assignedOptions[chr(self._lastOption)] = option.title
                self._lastOption+=1
            else:
                #throw out of bounds error
                break

    def display_menu(self):
        for option in self.assignedOptions:
            print(option,')',self.assignedOptions[option])
    
    def display_selection_message(self):
        print("\nPlease make a selection")

    def valid_selection(self,selection):
        if Selection.greater_than_one(selection):
            self.display_selection_message()
            return False
        elif not Selection.within_bounds(ord(selection),self._firstOption,self._lastOption):
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
