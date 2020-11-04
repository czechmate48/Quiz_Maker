# keys.py


class Keys:

    """Abstract parent class used for polymorphism in children"""

    def __init__(self):
        pass

    @staticmethod
    def get_keys():
        k = Keys()
        return [k.__dict__[var] for var in k.__dict__]
