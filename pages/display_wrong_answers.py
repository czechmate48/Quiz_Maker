from memory.cache import AnswerSheetCache, CacheCat
from pages.next_page import NextPage
from pages.page import Page, PageOptions


class DisplayWrongAnswers(Page):

    def __init__(self):
        pass

    def display(self):
        self.calculate_and_print_score()
        self.show_answers()

    def calculate_and_print_score(self):
        _correct_answers: float = 0
        _total_answers: float = 0
        for _answer in AnswerSheetCache.get_all_values_in_cache(CacheCat.answer_sheet):
            _total_answers = _total_answers + 1
            if _answer.get_status(): # Means if _answer.get_status() == True
                _correct_answers = _correct_answers + 1
        _final_score = _correct_answers/_total_answers * 100
        _final_score = round(_final_score, 2)
        print("\n########################")
        print("# SCORE                #")
        print("########################\n")
        print("FINAL SCORE: ", _final_score, "%")
        print("TOTAL QUESTIONS: ", _total_answers)
        print("TOTAL CORRECT ANSWERS: ", _correct_answers)

    def show_answers(self):
        print("\n########################")
        print("# ANSWERS              #")
        print("########################\n")
        for _answer in AnswerSheetCache.get_all_values_in_cache(CacheCat.answer_sheet):
            if not _answer.get_status():  # Means if _answer.get_status() == False
                print("WRONG:   ", _answer.get_inquiry(), "| CORRECT ANSWER: ", _answer.get_correct_answer(),
                      "| YOUR ANSWER: ", _answer.get_user_answer())
            else:
                print("CORRECT: ", _answer.get_inquiry(), "| CORRECT ANSWER: ", _answer.get_correct_answer())

    def get_next_page(self):
        return NextPage(PageOptions.home)