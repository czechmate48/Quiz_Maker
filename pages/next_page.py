from pages.page import PageOptions


class NextPage:

    def __init__(self, page_name=PageOptions.home, file_path='', question=''):
        self.page_name = page_name
        self.file_path = file_path
        self.question = question
