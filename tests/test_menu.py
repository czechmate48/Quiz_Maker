#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from page import Home, Edit, Page_Factory, Page_Options
from menu import Menu,Menu_Factory,Option,Selection
from question import Question_Keys,Question_Factory
from question_prompt import Question_Prompt
from cache  import Question_Cache,Cacheable,Cache_Cat
from storage import Storage

file_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"

question_factory=Question_Factory()
Storage.cache_elements_in_file(Question_Keys.get_keys(),file_path,Cache_Cat.question,question_factory)

#Need to create the quiz_cache

page=Page_Factory.create_page(Page_Options.home_screen)
while True:
    page=page.display()
