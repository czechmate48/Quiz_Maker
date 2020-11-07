#!/bin/bash

# Install Commands 
# 1) dos2unix Install.sh
# 2) sudo ./Install.sh

# Install python 3.8
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8

# Data directory
data_path='/var/lib/quiz_maker'
sudo mkdir -p $data_path

# Create file_path.txt
file_paths="$data_path/file_paths.txt"
chmod ugo=rwx $file_paths
sudo touch $file_paths

# Load quizzez.qz into file_path.txt
quiz_file_path="quiz_file_path=$data_path/quizzes.qz="
sudo echo $quiz_file_path > $file_paths

# Load questions.qst into file_path.txt
question_file_path="question_file_path=$data_path/questions.qst="
sudo echo $question_file_path > $file_paths

# Create a bash command
command_path="/bin/quizmaker"
sudo touch $command_path
sudo chmod ugo=rwx $command_path
sudo echo "python3.8 $data_path/main/quiz_maker.py" > $command_path

# Move project folder to Data directory
sudo cp -r data $data_path
sudo cp -r elements $data_path
sudo cp -r format $data_path
sudo cp -r main $data_path
sudo cp -r memory $data_path
sudo cp -r pages $data_path
sudo cp -r README.md $data_path
