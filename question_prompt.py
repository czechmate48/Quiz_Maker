#question_prompt

from question import Question,Question_Factory,Question_Styles,Question_Keys,Question_IO

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
        _question.update((_qstyle,_qinquiry,_qchoices,_qanswer),Question_Keys.get_keys(),True) #generate new ID
        
        #FIXME -> Do we want to call IO here? Should this be managed by class that manages all questions?        
        
        Question_IO.append_question_to_file(_path,_question)
    
    @staticmethod
    def remove_question(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
        _selection = Question_IO.prompt_remove_question(_path)
        
