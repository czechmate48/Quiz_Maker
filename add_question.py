#add_question.py

from menu import Menu,Option,Selection
from question import Question_Styles

def get_question_style():
    
    options = [
            Option(Question_Styles.true_false),
            Option(Question_Styles.fill_in_the_blank),
            Option(Question_Styles.multiple_choice)
            ]
    menu = Menu(options)
    menu.display_header_two("Please select a question style\n")
    menu.display_menu()
    selection = chr(menu.optionLim+1)
    while not menu.valid_selection(selection):
        selection = input().upper()
    return menu.assignedOptions[selection]

def get_question_inquiry():
    options=[]
    menu=Menu(options)
    menu.display_header_two("Please input a question")
    selection = input()
    return selection

question_style = get_question_style()
question_inquiry = get_question_inquiry()

print(question_inquiry)
