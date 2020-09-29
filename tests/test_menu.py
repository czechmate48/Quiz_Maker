# test_menu.py

"""test file to generate a new menu"""

from link_imports import link_parent_directory

link_parent_directory()
from pages.next_page import NextPage
from pages.page_factory import PageFactory
from pages.home import PageOptions
from storage import Storage

# FIXME -> Need to remove '=' at end of config filepaths. For some reason I keep getting a /n at the
# FIXME -> end of the filepath even though tried trimming it with rstrip()

question_file_path = Storage.get_config_value('/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'question_file_path')

initial_page = NextPage(PageOptions.home)
page = PageFactory.create_page(initial_page)

while True:
    page.display()
    next_page = page.get_next_page()  # NextPage Object
    page = PageFactory.create_page(next_page)  # Create the next page

    # The edit_specific_question page is able to edit a specific question,
    # but it is not yet able to correctly update the question_file.
    # It seems to be removing the question from the question cache, but the
    # question file is not rewritten when the question is selected for being
    # edited. Need to make the question file update correctly after a question
    # is edited
