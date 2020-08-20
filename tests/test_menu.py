#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from menu import Menu,Menu_Factory,Option,Selection
from question_prompt import Question_Prompt

options=[
    Option("Take practice quiz"),Option("Read question sheet"),Option("Add new question"),
    Option("Remove question"),Option("Quit")
    ]

selection = Menu_Factory.run_option_menu(options,"please make a selection","QUIZ MAKER 1.0")
if selection.letter == "C":
    Question_Prompt().add_question()
elif selection.letter == "D":
    Question_Prompt().remove_question()
