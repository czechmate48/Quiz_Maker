# storage.py

from element import ElementStyle
from file_manager import FileWriter, FileReader
from cache import Cacheable
import ast


class Storage(FileWriter, FileReader):

    @classmethod
    def cache_elements_in_file(cls, keys, file_path, cache_name, element_factory):
        """Clears a cache and overwrites it with the lines in the file"""

        Cacheable.delete_cache(cache_name)
        _lines = cls.get_lines(file_path)
        if len(_lines) > 0:
            _elements = []
            for line in _lines:
                if cls.is_blank_line(line):  # Prevents blank lines from creating an empty element
                    continue
                _elements.append(cls.read_element_from_file(line, keys, element_factory))
            for element in _elements:
                Cacheable.add_value_to_cache(cache_name, element)
        else:
            Cacheable.create_cache(cache_name)

    @classmethod
    def is_blank_line(cls, line):
        if line == "\n":
            return True
        else:
            return False

    @classmethod
    def read_element_from_file(cls, _line, _keys, element_factory):
        _values = []
        try:
            _raw_content = ast.literal_eval(_line)
            for key in _keys:
                _values.append(_raw_content[key])
            return element_factory.create_element(ElementStyle.generic, _values, _keys, False)
        except EOFError:
            #  Prevents an error if there is a blank line in the file
            print("End of File Error")


    @classmethod
    def append_element_to_file(cls, file_path, element):
        cls.append_line(element, file_path)

    @classmethod
    def overwrite_elements_to_file(cls, file_path, elements):
        cls.overwrite_file(elements, file_path)

    @classmethod
    def get_config_value(cls, _file_path, _config_value):
        _lines = cls.get_lines(_file_path)
        for _line in _lines:
            _values = _line.split("=")
            if _values[0] == _config_value:
                _values[1] = str(_values[1])  # convert to string
                _values[1].rstrip('\n')  # removes /n at end of variable
                return _values[1]
