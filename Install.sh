#!/bin/bash

#Install python 3.8
sudo apt-get install python3.8

#Declare file paths
data_path = "/var/lib/quiz_maker"
file_paths = "$data_path/file_paths.txt"
quizzes = "$data_path/quizzes.qz"
quiz_file_path = "quiz_file_path=/home/$USER/Documents/python/programs/Quiz_Maker/data/quizzes.qz="
question_file_path = "question_file_path=/home/$USER/Documents/python/programs/Quiz_Maker/data/questions.qst="

#Create files
mkdir $data_path
touch $file_paths
touch $quizzes

#Load data into files
echo $quiz_file_path > $file_paths
echo $question_file_path > $file_paths
