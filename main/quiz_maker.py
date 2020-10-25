# quiz_maker.py

from link_imports import link_parent_directory

link_parent_directory()
from pages.next_page import NextPage
from pages.page_factory import PageFactory
from pages.home import PageOptions
from memory.storage import Storage

# FIXME -> Need to remove '=' at end of config filepaths. For some reason I keep getting a /n at the
# FIXME -> end of the filepath even though tried trimming it with rstrip()
# FIXME -> Create bash script to create file_path.txt and set locations
# FIXME -> Create bash script to create quizzes.qz and set locations

question_file_path = Storage.get_config_value('/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'question_file_path')

initial_page = NextPage(PageOptions.home)
page = PageFactory.create_page(initial_page)

while True:
    page.display()
    next_page = page.get_next_page()  # NextPage Object
    page = PageFactory.create_page(next_page)  # Create the next page
