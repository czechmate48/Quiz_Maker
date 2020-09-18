# file_manager.py

class FileWriter:
    
    def __init__(self):
        pass

    @classmethod
    def create_new_file(cls, file_path="/"):
        _file = open(file_path, "x")

    @classmethod
    def write_lines(cls, lines, file_path):
        for line in lines:
            cls.write_line(line, file_path)

    @classmethod
    def append_line(cls, line, file_path):
        with open(file_path, 'a') as fw:
            print(line, file=fw)

    @classmethod
    def overwrite_file(cls, _lines, _file_path):
        with open(_file_path, 'w') as fw:
            print(_lines[0], file=fw)
        _lines.pop(0)
        for _line in _lines:
            FileWriter.append_line(_line, _file_path)


class FileReader:
    
    def __init__(self):
        pass
    
    @classmethod    
    def get_lines(cls, file_path):
        with open(file_path) as fi:
            _lines = [line for line in fi.readlines()]
        return _lines
