#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from menu import Menu,Option,Selection

options=[
    Option("Take practice quiz","C:"),Option("Read question sheet","C:"),Option("Add new question","C:"),
    Option("Remove question","C:"),Option("Quit","C:")
    ]
menu = Menu(options)
selection = chr(menu.optionLim+1)
menu.display_header_one('VIM LEARNER 0.0')
menu.display_menu()

while not menu.valid_selection(selection):
    selection = input().upper()
