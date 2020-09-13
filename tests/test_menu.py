#test_menu.py
'''test file to generate a new menu'''

from link_imports import link_parent_directory
link_parent_directory()

from page import Home, Edit, PageFactory, PageOptions
from menu import Menu,Menu_Factory,Option,Selection
from question import QuestionKeys,QuestionFactory
from question_prompt import QuestionPrompt
from quiz import QuizKeys,QuizFactory
from cache  import QuestionCache,Cacheable,CacheCat
from storage import Storage

question_file_path="/home/czechmate/Documents/python/programs/Quiz_Maker/data/questions.qst"
quiz_file_path="/home/czechmate/Documents/python/programs/Quiz_Maker/data/quizes.qz"

question_factory=QuestionFactory()
Storage.cache_elements_in_file(QuestionKeys.get_keys(), question_file_path, CacheCat.question, question_factory)
quiz_factory=QuizFactory()
Storage.cache_elements_in_file(QuizKeys.get_keys(), quiz_file_path, CacheCat.quiz, quiz_factory)

page=PageFactory.create_page(PageOptions.home_screen)
while True:
    page=page.display()
