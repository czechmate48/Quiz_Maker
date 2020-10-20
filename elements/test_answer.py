# test_answer.py
from dataclasses import dataclass

from elements.element import Element
from elements.keys import Keys
from elements.question import Question
from format.menu import MenuFactory, Option


@dataclass
class TestAnswerKeys(Keys):

    uid: str = "uid"
    user_answer: str = "user answer"
    inquiry: str = "inquiry"
    correct_answer: str = "correct answer"
    status: str = "status"  # Correct/Incorrect

    @staticmethod
    def get_keys():
        k = TestAnswerKeys()
        return [k.__dict__[var] for var in k.__dict__]


class TestAnswer(Element):

    def __init__(self, values, keys, generate_id, question):  # generate_id auto assigned in parent
        super(TestAnswer, self).__init__(values, keys, generate_id)
        self._question: Question = question  # a Question object
        self._user_answer: Option = ''

    def get_inquiry(self):
        return self.content[TestAnswerKeys.inquiry]

    def get_correct_answer(self):
        return self.content[TestAnswerKeys.correct_answer]

    def get_user_answer(self):
        _options = []
        for _choice in self._question.get_choices():
            _options.append(_choice)
        self._user_answer = MenuFactory.run_option_menu_no_sm(_options, self.get_inquiry())
        self._user_answer = self._user_answer.display_value
        return self._user_answer

    def get_status(self):
        return self.content[TestAnswerKeys.status]
