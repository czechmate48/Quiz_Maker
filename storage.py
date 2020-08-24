#storage.py

from element import Element_Factory
from file_manager import File_Writer, File_Reader
import ast

class Storage(File_Writer,File_Reader):

    @classmethod
    def read_element_from_file(cls,_line,_keys,element):
        '''gets an element from a line in a test file'''
        _raw_content=ast.literal_eval(_line)
        _values=[]
        for key in _keys:
            _values.append(_raw_content[key])
        return element.update(_values,_keys,False)

    @classmethod
    def append_element_to_file(cls,file_path,element):
        cls.append_line(element,file_path)

    @classmethod
    def overwrite_elements_to_file(cls,file_path,elements):
        cls.overwrite_file(elements,file_path)
