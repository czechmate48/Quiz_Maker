#standard_question.py
'''Used to standardize the implementation of question for use in 
projects that require standard true/false, multiple choice, and
fill in the blank questions'''

from question import Question

class Standard_Question(Question):

    #KEYS
    style="style"
    inquiry="inquiry"
    choices="choices"
    answer="answer"

    #STYLES
    true_false = 'TRUE/FALSE'
    multiple_choice='MULTIPLE CHOICE'
    fill_in_the_blank='FILL IN THE BLANK'
    styles = (true_false,multiple_choice,fill_in_the_blank)

