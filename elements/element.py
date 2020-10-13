# elements.element.py

"""Elements are components of the program that are essentially generated
as a dictionary. They can be prompted for after the class is inherited"""

from memory.cache import UniqueId
from elements.keys import Keys
from dataclasses import dataclass

@dataclass
class ElementStyle(Keys):

    generic: str = "generic"


class Element:

    def __init__(self, qvalues, qkeys, generate_id=True):
        self._values = []
        self._keys = []
        if generate_id:
            self.uid = id(self)
            self.uid = UniqueId.generate_uid(self.uid)
            self._values.append(self.uid)
        for value in qvalues:
            self._values.append(value)
        for key in qkeys:
            self._keys.append(key)
        self.content = self.merge_input(self._values, self._keys)

    def merge_input(self, qvalues, qkeys):
        _items = zip(qkeys,qvalues)
        return {item[0]: item[1] for item in _items}


class ElementFactory:
    """Element factory works as an object or a statically called class"""

    def __init__(self):
        pass

    def build_element(self, style, values=[], keys=[], generate_uid=True):
        pass

    @staticmethod
    def create_element(style, values=[], keys=[], generate_uid=True):
        pass
