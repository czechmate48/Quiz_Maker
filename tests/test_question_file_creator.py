#Question.py
import ast
from link_imports import link_parent_directory
link_parent_directory()
from file_manager import File_Reader,FileWriter
from question import Question, QuestionKeys,QuestionStyles,Question_Utility

#######
#MIGHT BE AN ISSUE WITH CHOICES TUPLE IN CREATION
test_file='test_file.txt'
q1_values=(QuestionStyles.true_false, 'Do you like food?', ('true', 'false'), 'true')
q2_values=(QuestionStyles.multiple_choice, 'Best part of the day.', ('morning', 'afternoon', 'night'), 'night')
q3_values=(QuestionStyles.fill_in_the_blank, 'America was discovered in ****', (''), '1492')
q1=Question(q1_values, QuestionKeys.get_keys())
q2=Question(q2_values, QuestionKeys.get_keys())
q3=Question(q3_values, QuestionKeys.get_keys())
questions=[q1,q2,q3]
for question in questions:
    _question = Question_Utility.get_question_as_dictionary(question)
    Question_Utility.write_line(_question,test_file)    
#######
lines = Question_Utility.get_lines(test_file)
all_questions=[]
for line in lines:
    all_questions.append(Question_Utility.get_question_from_line(line, QuestionKeys.get_keys()))
for question in all_questions:
    for value in question._values:
        print(value)
