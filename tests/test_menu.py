#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from menu import Menu,Option,Selection
from question_prompt import Question_Prompt

options=[
    Option("Take practice quiz","C:"),Option("Read question sheet","C:"),Option("Add new question","C:"),
    Option("Remove question","C:"),Option("Quit","C:")
    ]
menu = Menu(options)
selection = menu.initial_selection
menu.display_header_one('QUIZ MAKER 1.0')
menu.display_options()
selection = menu.get_user_selection()
if selection == "C":
    Question_Prompt().add_question()
elif selection == "D":
    Question_Prompt().remove_question()
