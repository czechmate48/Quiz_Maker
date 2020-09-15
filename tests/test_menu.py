# test_menu.py

"""test file to generate a new menu"""

from link_imports import link_parent_directory

link_parent_directory()

from page import PageFactory, PageOptions
from question import QuestionKeys, QuestionFactory
from quiz import QuizKeys, QuizFactory
from cache import CacheCat, QuizCache, QuestionCache
from storage import Storage

# FIXME -> Need to remove '=' at end of config filepaths. For some reason I keep getting a /n at the
# FIXME -> end of the filepath even though tried trimming it with rstrip()

question_file_path = Storage.get_config_value('/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'question_file_path')
quiz_file_path = Storage.get_config_value('/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'quiz_file_path')

question_factory = QuestionFactory()
Storage.cache_elements_in_file(QuestionKeys.get_keys(), question_file_path, CacheCat.question,
                               question_factory)

quiz_factory = QuizFactory()
Storage.cache_elements_in_file(QuizKeys.get_keys(), quiz_file_path, CacheCat.quiz, quiz_factory)

page = PageFactory.create_page(PageOptions.home_screen)
while True:
    page = page.display()
