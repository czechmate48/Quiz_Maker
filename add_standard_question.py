#add_standard_question.py

from menu import Menu,Option,Selection
from question import Question

def get_style():
    options = Option.generate_option_list(Question.styles)
    return run_option_menu(options,"\nPlease select a question style\n","\nWhat is the question style?\n")

def get_inquiry():
    options = Option.generate_option_list([]) #blank list for no  options
    return run_no_option_menu("Please input a question")

def get_choices(style):
    choices=[]
    if style == Question.multiple_choice:
        numChoices=get_num_choices()
        while numChoices > 0:
            print("please input a choice")
            choices.append(input())
            numChoices-=1
    elif style == Question.true_false:
        choices = ["true","false"]
    return choices

def get_num_choices():
    options=Option.generate_option_list([])
    menu=Menu(options)
    menu.display_header_two("Please input the number of choices")
    selection = input()
    try:
        selection = int(selection)
        return selection
    except ValueError:
        get_num_choices()
    
def get_answer(style,choices):
    if style == Question.multiple_choice:
        options = Option.generate_option_list(choices)
        return run_option_menu(options,"\nSelect correct answer","\nWhich choice is the correct answer?\n")
    elif style == Question.true_false:
        options = Option.generate_option_list(choices)
        return run_option_menu(options,"\nSelect correct answer","\nWhich choice is the correct answer\n")
    else:
        return run_no_option_menu("Please input the answer")

def run_option_menu(options,selection_message,header):
    menu = Menu(options)
    menu.selection_message = selection_message
    menu.display_header_two(header)
    menu.display_options()
    selection = menu.get_user_selection()
    return menu.assigned_options[selection]

def run_no_option_menu(header):
    menu = Menu([])
    menu.display_header_two(header)
    return menu.get_user_input()

qstyle = get_style()
qinquiry = get_inquiry()
qchoices = get_choices(qstyle)
qanswer = get_answer(qstyle,qchoices)
question = Question((qstyle,qinquiry,qchoices,qanswer),Question.standard_keys)
print(question.get_question_as_dictionary())
