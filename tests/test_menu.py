#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from page import Home, Edit, Page_Factory, Page_Options
from menu import Menu,Menu_Factory,Option,Selection
from question import Question_Keys,Question_Factory
from question_prompt import Question_Prompt
from quiz import Quiz_Keys,Quiz_Factory
from cache  import Question_Cache,Cacheable,Cache_Cat
from storage import Storage

question_file_path="/home/czechmate/Documents/python/programs/Quiz_Maker/data/questions.qst"
quiz_file_path="/home/czechmate/Documents/python/programs/Quiz_Maker/data/quizes.qz"

question_factory=Question_Factory()
Storage.cache_elements_in_file(Question_Keys.get_keys(),question_file_path,Cache_Cat.question,question_factory)
quiz_factory=Quiz_Factory()
Storage.cache_elements_in_file(Quiz_Keys.get_keys(),quiz_file_path,Cache_Cat.quiz,quiz_factory)

page=Page_Factory.create_page(Page_Options.home_screen)
while True:
    page=page.display()
