# Quiz Maker

Created by: Christopher N. Sefcik on 11/5/2020
Version 1.0: 11/5/2020

### Summary:
This application is used to make and take quizzes from the bash terminal

### Setup:
  1) Download the master folder
  2) Unzip the master folder
  3) Command: sudo apt-get install dos2unix
  4) Command: dos2unix Install.sh
  5) Command: sudo ./Install.sh
  6) Run the program by typing 'quizmaker'

### Configuration:

    Data Directory: /var/lib/quiz_maker; Holds all data for the project as well as configuration files
    
    file_paths.txt: /var/lib/quiz_maker/file_paths.txt; tells the location where to find quizzes.qz 
    
    quizzes.qz: Holds the name of all quizzes created by the user
    
    .qst: The extension used for any file that holds questions.
    
    /bin/quizmaker: The location of the bash command
