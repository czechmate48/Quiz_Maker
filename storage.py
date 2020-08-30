#storage.py

from element import Element_Factory, Element_Style
from file_manager import File_Writer, File_Reader
from cache import Cacheable
import ast

class Storage(File_Writer,File_Reader):

    @classmethod
    def cache_elements_in_file(cls,keys,file_path,cache_name,element_factory):
        _lines=cls.get_lines(file_path)
        if len(_lines) > 0:
            _elements=[]
            for line in _lines:
                _elements.append(cls.read_element_from_file(line,keys,element_factory))
            for element in _elements:
                Cacheable.add(cache_name,element)
        else: Cacheable.create(cache_name)

    @classmethod
    def read_element_from_file(cls,_line,_keys,element_factory):
        _raw_content=ast.literal_eval(_line)
        _values=[]
        for key in _keys:
            _values.append(_raw_content[key])
        return element_factory.create(Element_Style.generic,_values,_keys,False)

    @classmethod
    def append_element_to_file(cls,file_path,element):
        cls.append_line(element,file_path)

    @classmethod
    def overwrite_elements_to_file(cls,file_path,elements):
        cls.overwrite_file(elements,file_path)
