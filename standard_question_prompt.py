#standard_question_prompt

from menu import Menu,Option,Selection
from question import Question

class Standard_Question_Prompt():
    
    def __init__(self):
        pass

    def get_style(self):
        _options = Option.generate_option_list(Question.styles)
        _selection_message = "\nPlease select a question style\n"
        _header="\nWhat is the question style?\n"
        return self.run_option_menu(_options,_selection_message,_header)

    def get_inquiry(self):
        _header = "Please input a question"
        return self.run_no_option_menu(_header)

###############################

    def get_choices(self,_style):
        _choices=[]
        if _style == Question.multiple_choice:
            _num_choices=self.get_num_choices()
            _choices=self.get_choices_from_user(_num_choices)
        elif _style == Question.true_false:
            _choices = ["true","false"]
        return _choices

    def get_num_choices(self):
        _num_choices = -1
        while _num_choices == -1:
            try:
                _header="Please input the number of choices"
                _num_choices=self.run_no_option_menu(_header)
                _num_choices=int(_num_choices)
            except ValueError:
                _num_choices=-1
        return _num_choices

    def get_choices_from_user(self,_num_choices):
        _choices=[]
        while _num_choices > 0:
            print("please input a choice")
            _choices.append(input())
            _num_choices-=1
        return _choices

##################################

    def get_answer(self,_style,_choices):
        if _style == Question.multiple_choice:
            _options = Option.generate_option_list(_choices)
            _selection_message = "\nSelect correct answer"
            _header = "\nWhich choice is the correct answer?\n"
            return self.run_option_menu(_options,_selection_message,_header)
        elif _style == Question.true_false:
            _options = Option.generate_option_list(_choices)
            _selection_message = "\nSelect correct answer\n"
            _header="\nWhich choice is the correct answer?\n"
            return self.run_option_menu(_options,_selection_message,_header)
        else:
            _header = "Please input the answer"
            return self.run_no_option_menu(_header)

    def run_option_menu(self,options,selection_message,header):
        menu = Menu(options)
        menu.selection_message = selection_message
        menu.display_header_two(header)
        menu.display_options()
        selection = menu.get_user_selection()
        return menu.assigned_options[selection]

    def run_no_option_menu(self,header):
        menu = Menu([])
        menu.display_header_two(header)
        return menu.get_user_input()

    def get_question(self):
        _qstyle = self.get_style()
        _qinquiry = self.get_inquiry()
        _qchoices = self.get_choices(_qstyle)
        _qanswer = self.get_answer(_qstyle,_qchoices)
        _question = Question((_qstyle,_qinquiry,_qchoices,_qanswer),Question.standard_keys)
        return _question

prompt = Standard_Question_Prompt()
question = prompt.get_question()
print(question.get_question_as_dictionary())
