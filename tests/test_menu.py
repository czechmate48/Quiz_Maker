#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from page import Home, Edit, Page_Factory, Page_Types
from menu import Menu,Menu_Factory,Option,Selection
from question import Question_IO
from question_prompt import Question_Prompt,Question_Cache

file_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"
Question_IO.create_cache(file_path)

page=Page_Factory.create_page(Page_Types.home)
while True:
    selection=page.display()
    if (selection.letter=="B"):
        page=Page_Factory.create_page(Page_Types.edit)
