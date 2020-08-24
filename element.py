#element.py

'''Elements are components of the program that are essentially generated
as a dictionary. They can be prompted for after the class is inherited'''

class Element():

    def __init__(self, qvalues, qkeys, generate_id=True):
        self._values=[]
        self._keys=[]
        if generate_id:
            self.uid=id(self)
            self.uid=Unique_Id.generate_uid(self.uid)
            self._values.append(self.uid)
        for qvalue in qvalues:
            self._values.append(qvalue)
        for qkey in qkeys:
            self._keys.append(qkey)
        self.content=self.merge_input(qvalues,qkeys)

    def merge_input(self,qvalues,qkeys):
        items=zip(qkeys,qvalues)
        return {item[0]:item[1] for item in _items}

    def update(self,qvalues,qkeys,generate_id=False):
        return Element_Factory.create(qvalues,qkeys,generate_id)

class Element_Factory():

    def __init__():
        pass

    @staticmethod
    def create(style,values=[],keys=[],generate_uid=True):
        pass
