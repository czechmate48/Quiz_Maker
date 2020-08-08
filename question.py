#Question.py
'''Creates a question object that contains a variable for
each component of a question. Note that the question object
does NOT produce a dictionary by default, and will need to 
be converted to  a dictionary using the built in method'''

import ast

class Question_Styles():
    '''The question styles used for this specific program'''
    true_false="TRUE/FALSE"
    multiple_choice="MULTIPLE CHOICE"
    fill_in_the_blank="FILL IN THE BLANK"

class Question_Keys():
    '''The question keys used for this specific program'''
    style="style"
    inquiry="inquiry"
    choices="choices"
    answer="answer"

class Question():

    def __init__(self, qvalues, qkeys):
        self._values=[]
        for qvalue in qvalues:
            self._values.append(qvalue)
        self._keys=[]
        for qkey in qkeys:
            self._keys.append(qkey)

    @classmethod
    def get_question_from_line(cls,line,qkeys):
        _raw_content=ast.literal_eval(line)
        _qvalues=[]
        for _key in qkeys:
            _qvalues.append(_raw_content[_key])
        return Question(_qvalues,qkeys)
    
    def get_question_as_dictionary(self):
        _items=zip(self._keys,self._values) 
        _line={}
        for item in _items:
            _line[item[0]]=item[1]
        return _line
    
    def display():
        pass

class True_False(Question):
    pass

class Fill_In_The_Blank(Question):
    pass

class Multiple_Choice(Question):
    pass
