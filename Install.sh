#!/bin/bash
# Install python 3.8
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.8
# Data directory
data_path="/var/lib/quiz_maker" # The location of the data directory - STATIC, do not change as referenced in quiz_maker.py with same path
mkdir -p $data_path
# Create file_path.txt
file_paths="$data_path/file_paths.txt" #f ile_path.txt holds two variables that indicate where quizzes and their questions are saved
touch $file_paths
# Load quizzez.qz into file_path.txt
quiz_file_path="quiz_file_path=$data_path/quizzes.qz=" # Ignore '=' sign at end
echo $quiz_file_path > $file_paths
# Load questions.qst into file_path.txt
question_file_path="question_file_path=$data_path/questions.qst=" # Ignore '=' sign at end
echo $question_file_path > $file_paths
# Create a bash command
command_path="/bin/quiz-maker"
sudo touch $command_path
sudo echo "python3.8 $data_path/Quiz_Maker/main/quiz_maker.py" > command_path
# Move project folder to Data directory
cp -r data $data_path
cp -r elements $data_path
cp -r format $data_path
cp -r main $data_path
cp -r memory $data_path
cp -r pages $data_path
cp -r README.md $data_path
