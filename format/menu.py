# menu.py

"""This file creates a menu. It allows up to 25 menu options
with the value A-Z. Each selection will need to reference a seperate
file that contains the next set of code."""

###########################
from typing import Final
from memory.cache import UniqueId


class Menu:
    """Menu brings in a set of options and converts them
    into a dictionary - [selection variable,option]"""

    def __init__(self, options):
        """requires an option object from Option class"""
        self.first_option: Final = 65  # Used as a constant, starting ascii 65 (A)
        self._last_option = self.first_option
        self._option_lim: Final = 90  # Limited to 25 menu options
        self.assigned_options = {}  # options assigned a corresponding letter
        for option in options:
            if self._last_option < self._option_lim:
                self.assigned_options[chr(self._last_option)] = option
                option.set_letter(chr(self._last_option))
                self._last_option += 1
            else:
                # throw out of bounds error
                break
        self.initial_selection = chr(self._option_lim + 1)  # initial user selection used to launch loop
        self.selection_message = "\nPlease make a selection"  # Can be overridden for customization

    ###############

    def display_options(self):
        for option in self.assigned_options:
            print(option, ')', self.assigned_options[option].display_value)

    def display_selection_message(self):
        print(self.selection_message)

    def display_title(self, header):
        for x in header:
            print('#', end="")
        print('\n', header)
        for x in header:
            print('#', end="")
        print('\n', end="")

    def display_space(self):
        print('')

    def display_header(self, header):
        print(header)

    ###############

    def get_user_input(self):
        """Used when there are no options"""
        return input()

    def get_user_selection(self):
        """returns the option object selected by the user"""
        _selection = self.initial_selection
        while not self.check_valid_mc_selection(_selection):
            _selection = input().upper()
        return self.assigned_options[_selection]

    def check_valid_mc_selection(self, selection):
        if Selection.is_empty(selection):
            return False
        elif Selection.greater_than_one(selection):
            return False
        elif not Selection.within_bounds(ord(selection), self.first_option, self._last_option):
            return False
        elif not Selection.is_unicode(ord(selection)):  # lower and upper unicode values
            return False
        else:
            return True

    def get_yes_no_selection(self):
        _selection = input()
        while not Selection.is_yesno(_selection):
            _selection = input()
        _selection = _selection.lower()
        return _selection


#############################

class MenuFactory:

    @staticmethod
    def run_option_menu(options, selection_message, header):
        menu = Menu(options)
        menu.selection_message = selection_message
        menu.display_space()
        menu.display_header(header)
        menu.display_options()
        menu.display_selection_message()
        menu.display_space()
        return menu.get_user_selection()  # returns an option object, not a display_value

    @staticmethod
    def run_option_menu_no_sm(options, header):
        menu = Menu(options)
        menu.display_space()
        menu.display_header(header)
        menu.display_options()
        menu.display_space()
        return menu.get_user_selection()

    @staticmethod
    def run_no_option_menu(header):
        menu = Menu([])
        menu.display_space()
        menu.display_header(header)
        return menu.get_user_input()

    @staticmethod
    def run_yes_no_menu(header):
        menu = Menu([])
        menu.display_space()
        menu.display_header(header)
        return menu.get_yes_no_selection()


##############################

class Option:

    def __init__(self, display_value, link_uid=-1):  # link_uid of -1 means no link
        self.uid = UniqueId.generate_uid(id(self))
        self.display_value = display_value
        self.linked_uid = link_uid
        self.letter = "A"  # Updated to correct letter in Menu.py

    def set_letter(self, letter):
        self.letter = letter


class OptionFactory:
    """linked options connect the option UID with another UID, unlinked options
    simply display a display_value"""

    @staticmethod
    def generate_linked_options(display_values, uids):
        _values = zip(display_values, uids)
        return [Option(value[0], value[1]) for value in _values]

    @staticmethod
    def generate_unlinked_options(display_values):
        return [Option(value) for value in display_values]


##############################

class Selection:
    """Utility class that provides static methods used to make determinations
    about the user selection"""

    @staticmethod
    def greater_than_one(string):
        return len(string) > 1

    @staticmethod
    def within_bounds(value, lower, upper):
        return lower <= value < upper

    @staticmethod
    def is_unicode(value):
        return 0 < value < 0x10FFF

    @staticmethod
    def is_empty(string):
        return len(string) == 0

    @staticmethod
    def is_yesno(string):
        string = string.lower()
        return string == 'y' or string == "yes" or string == 'n' or string == "no"
