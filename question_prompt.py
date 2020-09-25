# question_prompt

from menu import Menu_Factory, Option_Factory
from question import Question, QuestionFactory, QuestionStyles, QuestionKeys, QuestionIO
from cache import CacheCat, QuestionCache
from storage import Storage


class QuestionPrompt:

    def __init__(self):
        pass

    @staticmethod
    def add_question(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
        _qstyle = Question.prompt_for_style()
        _question = QuestionFactory.create_element(_qstyle)  # generate ID
        _qinquiry = _question.prompt_for_inquiry()
        _qchoices = _question.prompt_for_choices()
        _qanswer = _question.prompt_for_answer(_qchoices)
        _question.update((_question.uid, _qstyle, _qinquiry, _qchoices, _qanswer), QuestionKeys.get_keys())
        QuestionCache.add_value_to_cache(CacheCat.question, _question)
        Storage.append_element_to_file(_question.content, _path)

    @staticmethod
    def remove_question(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
        _questions = QuestionCache.get_all_values_in_cache(CacheCat.question)
        _uids = [question.get_uid for question in _questions]
        _inquiries = [question.get_inquiry() for question in _questions]
        _options = Option_Factory.generate_linked_options(_inquiries, _uids)
        _selection_message = "Please select a question"
        _header = "Which question would you like to remove?"
        _selected_option = Menu_Factory.run_option_menu(_options, _selection_message, _header)
        _selected_uid = _selected_option.linked_uid
        _question_to_delete = QuestionPrompt.get_matching_question(_questions, _selected_uid)
        QuestionCache.remove_value_from_cache(CacheCat.question, _question_to_delete)
        QuestionIO.overwrite_questions_to_file(_path, QuestionCache.get_all_values_in_cache(CacheCat.question))
        QuestionCache.print_cache(CacheCat.question)

    @classmethod
    def get_matching_question(cls, _questions, _uid):
        for question in _questions:
            if question.get_uid == _uid:
                return question
