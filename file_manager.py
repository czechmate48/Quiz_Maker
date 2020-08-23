#file_manager.py

class File_Writer():
    
    def __init__(self):
        pass

    @staticmethod
    def write_lines(lines,file_path):
        for line in lines:
            self.write_line(line,file_path)

    @staticmethod
    def append_line(line,file_path):
        with open(file_path,'a') as fw:
            print(line,file=fw)

    @staticmethod
    def overwrite_file(_lines,_file_path):
        with open(_file_path,'w') as fw:
            print(_lines[0],file=fw)
        _lines.pop(0)
        for _line in _lines:
            File_Writer.append_line(_line,_file_path)

class File_Reader():
    
    def __init__(self):
        pass

    @staticmethod
    def get_lines(file_path):
        with open(file_path) as fi:
            _lines=[line for line in fi.readlines()]
        return _lines

