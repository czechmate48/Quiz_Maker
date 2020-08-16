#question_prompt

from question import Question,Question_Factory,Question_Styles,Question_Keys,Question_Utility

class Question_Prompt():

    def __init__(self):
        pass

    @staticmethod
    def prompt(_path="/home/czechmate/Documents/python/programs/Quiz_Maker/tests/test_file.txt"):
        _qstyle = Question.prompt_for_style()
        _question = Question_Factory.create_question(_qstyle)
        _all_question_uids = Question_Utility.get_all_question_values_by_key(Question_Keys.uid,_path)
        _question.set_uid(_question._uid,_all_question_uids)  
        _qinquiry = _question.prompt_for_inquiry() 
        _qchoices = _question.prompt_for_choices()
        _qanswer = _question.prompt_for_answer(_qchoices)
        _qvalues = (_qstyle,_qinquiry,_qchoices,_qanswer)
        _question.update((_qstyle,_qinquiry,_qchoices,_qanswer),Question_Keys.get_keys())
        Question_Utility.append_question_to_file(_path,_question)

