#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from page import Home, Edit, Page_Factory, Page_Options
from menu import Menu,Menu_Factory,Option,Selection
from question import Question_Keys
from question_prompt import Question_Prompt
from cache  import Question_Cache,Cacheable,Cache_Cat

file_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"

#FIXME -> The cache is not coverting the element into its appropriate form. This is because
# there is not a child instantiation being passed into cacheable method, so it doesn't know
# how to reference the appropriate element_factory. 

Cacheable.create_cache(Question_Keys.get_keys(),file_path,Cache_Cat.question)
Question_Cache.print_cache(Cache_Cat.question)

#Need to create the quiz_cache

page=Page_Factory.create_page(Page_Options.home_screen)
while True:
    selection=page.display()
    if (selection.letter=="B"):
        page=Page_Factory.create_page(Page_Types.edit)
