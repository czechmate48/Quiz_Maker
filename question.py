#question.py
'''Creates a question object that contains a variable for
each component of a question. Note that the question object
does NOT produce a dictionary by default, and will need to 
be converted to  a dictionary using the built in method'''

import ast

class Question():

    style="style"
    inquiry="inquiry"
    choices="choices"
    answer="answer"
    standard_keys=(style,inquiry,choices,answer)

    true_false="TRUE/FALSE"
    multiple_choice="MULTIPLE CHOICE"
    fill_in_the_blank="FILL IN THE BLANK"
    styles = (true_false,multiple_choice,fill_in_the_blank)
    
    def __init__(self, qvalues, qkeys):
        self._values=[]
        for qvalue in qvalues:
            self._values.append(qvalue)
        self._keys=[]
        for qkey in qkeys:
            self._keys.append(qkey)

###############################
#Reading questions from a file#
###############################

    @classmethod
    def get_question_from_line(cls,line,qkeys):
        '''Get a question from a line in a text file.
        The line must be saved in dictionary format
        as this method derives keys & values'''
        _raw_content=ast.literal_eval(line)
        _qvalues=[]
        for _key in qkeys:
            _qvalues.append(_raw_content[_key])
        return Question(_qvalues,qkeys)
    
######################
#Converting questions#
######################

    def get_question_as_dictionary(self):
        _items=zip(self._keys,self._values) 
        _line={}
        for item in _items:
            _line[item[0]]=item[1]
        return _line
    
    def display():
        pass

class Style():
    pass
    
    #A style has a uniform key (style)
    #A style has a unique value: multiple choices,true/false
    #A style has a way to be prompted for
    #A style is displayable [interface?]
    #A style is promptable [interface?]

class Inquiry():
    pass

class Choice():
    pass

class Answer():
    pass

class True_False(Question):
    pass

class Fill_In_The_Blank(Question):
    pass

class Multiple_Choice(Question):
    pass
