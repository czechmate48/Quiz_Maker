# test_menu.py

"""test file to generate a new menu"""

from link_imports import link_parent_directory

link_parent_directory()
from pages.next_page import NextPage
from pages.page_factory import PageFactory
from pages.home import PageOptions
from memory.storage import Storage

# FIXME -> Need to remove '=' at end of config filepaths. For some reason I keep getting a /n at the
# FIXME -> end of the filepath even though tried trimming it with rstrip()

question_file_path = Storage.get_config_value('/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'question_file_path')

initial_page = NextPage(PageOptions.home)
page = PageFactory.create_page(initial_page)

while True:
    page.display()
    next_page = page.get_next_page()  # NextPage Object
    page = PageFactory.create_page(next_page)  # Create the next page

    #  10/5 Start with 'choose_quiz_to_take'. The logic for the page is done except for
    #  where the program should go after selecting a quiz. You need to creating a
    #  'TakeQuiz' component of the program that asks questions, stores the score,
    #  and provides a final result
    #
    #  10/13 Started creating the "take_quiz.py" page. Need to create a test_answer.py object
    #  when an answer is inputted by the user. Then save the test_answer.py to a cache.
