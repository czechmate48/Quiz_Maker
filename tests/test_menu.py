# test_menu.py

"""test file to generate a new menu"""

from link_imports import link_parent_directory

link_parent_directory()

from pages.home import PageOptions, HomeFactory

from storage import Storage

# FIXME -> Need to remove '=' at end of config filepaths. For some reason I keep getting a /n at the
# FIXME -> end of the filepath even though tried trimming it with rstrip()

question_file_path = Storage.get_config_value('/home/czechmate/Documents/python/programs/Quiz_Maker/data/file_paths.txt', 'question_file_path')

page = HomeFactory.create_page(PageOptions.home)
while True:
    page.display()
    next_page = page.get_next_page()

    # Start here
    # Look how home is structured. Unfortunately you are passing file_paths
    # and other data when a next_page is obtained. Need to figure out some
    # way to pass that data. Maybe create an Next_Page class that holds all
    # of that data. Every page class except home.py needs work.
