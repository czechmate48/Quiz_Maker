#question_prompt

from question import Question,Question_Factory,Question_Styles,Question_Keys,Question_IO
from cache import Question_Cache

class Question_Prompt():

    def __init__(self):
        pass

    @staticmethod
    def add_question(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
        _qstyle = Question.prompt_for_style()
        _question = Question_Factory.create_question(_qstyle) #generate ID
        _qinquiry = _question.prompt_for_inquiry() 
        _qchoices = _question.prompt_for_choices()
        _qanswer = _question.prompt_for_answer(_qchoices)
        _question.update((_question.uid,_qstyle,_qinquiry,_qchoices,_qanswer),Question_Keys.get_keys())
        Question_Cache.add(_question)
    
    @staticmethod
    def remove_question(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
       pass 
