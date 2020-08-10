#add_standard_question.py

from menu import Menu,Option,Selection
from standard_question import Standard_Question

def get_style():
    options = [Option(style) for style in Standard_Question.styles]
    menu = Menu(options)
    menu.display_header_two("Please select a question style\n")
    menu.display_menu()
    selection = chr(menu.optionLim+1)
    while not menu.valid_selection(selection):
        selection = input().upper()
    return menu.assignedOptions[selection]

def get_inquiry():
    options=[]
    menu=Menu(options)
    menu.display_header_two("Please input a question")
    selection = input()
    return selection

def get_choices(style):
    if style == Standard_Question.multiple_choice:
        numChoices=get_num_choices()
        choices=[]
        while numChoices > 0:
            print("please input a choice")
            choices.append(input())
            numChoices-=1
        return choices
    else:
        return

def get_num_choices():
    options=[]
    menu=Menu(options)
    menu.display_header_two("Please input the number of choices")
    selection = input()
    try:
        selection = int(selection)
        return selection
    except ValueError:
        get_num_choices()
    
question_style = get_style()
question_inquiry = get_inquiry()
question_choices = get_choices(question_style)
print(question_choices)

