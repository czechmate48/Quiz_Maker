from pages.page import PageOptions


class NextPage:

    def __init__(self, next_page_name=PageOptions.home, file_path='', question=''):
        self.next_page_name = next_page_name
        self.file_path = file_path
        self.question = question
