#!/bin/bash

#Install python 3.8
sudo apt-get install python3.8

#Data directory
data_path = "/var/lib/quiz_maker" #The location of the data directory - STATIC, do not change as referenced in quiz_maker.py with same path
mkdir $data_path

#file_paths file
file_paths = "$data_path/file_paths.txt" #The file indicating the path where quizzes and their questions are saved
touch $file_paths
quiz_file_path = "quiz_file_path=$data_path/quizzes.qz=" # Ignore '=' sign at end
question_file_path = "question_file_path=$data_path/questions.qst=" # Ignore '=' sign at end
echo $quiz_file_path > $file_paths
echo $question_file_path > $file_paths




