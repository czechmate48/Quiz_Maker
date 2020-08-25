#question_prompt

from menu import Menu_Factory, Option_Factory
from question import Question,Question_Factory,Question_Styles,Question_Keys,Question_IO
from cache import Cache_Cat, Question_Cache

class Question_Prompt():

    def __init__(self):
        pass

    @staticmethod
    def add_question(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
        _qstyle = Question.prompt_for_style()
        _question = Question_Factory.create(_qstyle) #generate ID
        _qinquiry = _question.prompt_for_inquiry() 
        _qchoices = _question.prompt_for_choices()
        _qanswer = _question.prompt_for_answer(_qchoices)
        _question.update((_question.uid,_qstyle,_qinquiry,_qchoices,_qanswer),Question_Keys.get_keys())
        Question_Cache.add(Cache_Cat.question,_question)

        Storage.append_element_to_file(_question.content,_path)
        

    @staticmethod
    def remove_question(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
        _questions = Question_Cache.get_all(Cache_Cat.question)
        _uids = [question.get_uid for question in _questions]
        _inquiries = [question.get_inquiry() for question in _questions]
        _options=Option_Factory.generate_linked_options(_inquiries,_uids)
        _selection_message="Please select a question"
        _header="Which question would you like to remove?"
        _selected_option = Menu_Factory.run_option_menu(_options,_selection_message,_header)
        _selected_uid = _selected_option.linked_uid
        _question_to_delete = Question_Prompt.get_matching_question(_questions,_selected_uid)
        Question_Cache.remove(Cache_Cat.question,_question_to_delete)
        Question_IO.overwrite_questions_to_file(_path,Question_Cache.get_all(Cache_Cat.question))
        Question_Cache.print_cache(Cache_Cat.question)

    @classmethod
    def get_matching_question(cls,_questions,_uid):
        for question in _questions:
            if question.get_uid==_uid:
                return question
