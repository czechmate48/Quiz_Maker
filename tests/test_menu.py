# test_menu.py

"""test file to generate a new menu"""

from link_imports import link_parent_directory

link_parent_directory()


from question import QuestionKeys, QuestionFactory
from quiz import QuizKeys, QuizFactory
from cache import CacheCat
from storage import Storage
from page import PageOptions, PageFactory

# FIXME -> Need to remove '=' at end of config filepaths. For some reason I keep getting a /n at the
# FIXME -> end of the filepath even though tried trimming it with rstrip()

question_file_path = Storage.get_config_value('/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'question_file_path')

page = PageFactory.create_page(PageOptions.home_screen)
while True:
    page = page.display()
