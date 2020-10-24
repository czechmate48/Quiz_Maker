from memory.cache import AnswerSheetCache, CacheCat
from pages.next_page import NextPage
from pages.page import Page, PageOptions


class DisplayWrongAnswers(Page):

    def __init__(self):
        self._correct_answers: float = 0
        self._total_answers: float = 0
        self._final_score: float = 0

    def display(self):
        self.calculate_score()
        self.print_score()
        self.print_answers()
        self.delete_cache()

    def calculate_score(self):
        for _answer in AnswerSheetCache.get_all_values_in_cache(CacheCat.answer_sheet):
            self._total_answers = self._total_answers + 1
            if _answer.get_status(): # Means if _answer.get_status() == True
                self._correct_answers = self._correct_answers + 1
        self._final_score = self._correct_answers/self._total_answers * 100
        self._final_score = round(self._final_score, 2)

    def print_score(self):
        print("\n########################")
        print("# SCORE                #")
        print("########################\n")
        print("FINAL SCORE: ", self._final_score, "%")
        print("TOTAL QUESTIONS: ", self._total_answers)
        print("TOTAL CORRECT ANSWERS: ", self._correct_answers)

    def print_answers(self):
        print("\n########################")
        print("# ANSWERS              #")
        print("########################\n")
        for _answer in AnswerSheetCache.get_all_values_in_cache(CacheCat.answer_sheet):
            if not _answer.get_status():  # Means if _answer.get_status() == False
                print("WRONG:   ", _answer.get_inquiry(), "| CORRECT ANSWER: ", _answer.get_correct_answer(),
                      "| YOUR ANSWER: ", _answer.get_user_answer())
            else:
                print("CORRECT: ", _answer.get_inquiry(), "| CORRECT ANSWER: ", _answer.get_correct_answer())

    def delete_cache(self):
        AnswerSheetCache.delete_cache(CacheCat.answer_sheet)

    def get_next_page(self):
        return NextPage(PageOptions.home)
