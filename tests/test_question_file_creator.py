#Question.py
import ast
from link_imports import link_parent_directory
link_parent_directory()
from file_manager import File_Reader,File_Writer 
from question import Question

#######
#MIGHT BE AN ISSUE WITH CHOICES TUPLE IN CREATION
test_file='test_file.txt'
keys=[Question.style,Question.inquiry,Question.choices,Question.answer]
q1_values=(Question.true_false,'Do you like food?',('true','false'),'true')
q2_values=(Question.multiple_choice,'Best part of the day.',('morning','afternoon','night'),'night')
q3_values=(Question.fill_in_the_blank,'America was discovered in ****',(''),'1492')
q1=Question(q1_values,keys)
q2=Question(q2_values,keys)
q3=Question(q3_values,keys)
questions=[q1,q2,q3]
file_writer = File_Writer(test_file)
for question in questions:
    file_writer.write_line(question.get_question_as_dictionary())    
#######
file_reader=File_Reader(test_file)
lines=file_reader.get_lines()
all_questions=[]
for line in lines:
    all_questions.append(question.get_question_from_line(line,keys))
for question in all_questions:
    for value in question._values:
        print(value)
