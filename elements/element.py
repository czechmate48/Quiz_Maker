# elements.element.py

from memory.cache import UniqueId
from elements.keys import Keys
from dataclasses import dataclass

@dataclass
class ElementStyle(Keys):

    def __init__(self):
        pass

    generic: str = "generic"


class Element:

    """Element class encapsulates a dictionary item. The class is intended
    to be inherited from for creating the various components of the program"""

    def __init__(self, values, keys, generate_id=True):
        self._values = []
        self._keys = []
        if generate_id:
            self.uid = id(self)
            self.uid = UniqueId.generate_uid(self.uid)
            self._values.append(self.uid)
        for value in values:
            self._values.append(value)
        for key in keys:
            self._keys.append(key)
        self.content = self.merge_input(self._values, self._keys)

    def merge_input(self, values, keys):
        _items = zip(keys, values)
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
