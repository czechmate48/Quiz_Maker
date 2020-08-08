#file_manager.py

class File_Writer():
    def __init__(self,file_path):
        self._file_path = file_path

    def write_lines(self,lines):
        for line in lines:
            self.write_line(line)

    def write_line(self,line):
        with open(self._file_path,'a') as fw:
            print(line,file=fw)

class File_Reader():
    def __init__(self,file_path):
        self._file_path = file_path

    def get_lines(self):
        with open(self._file_path) as fi:
            self._lines=[line for line in fi.readlines()]
        return self._lines
