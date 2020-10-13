# keys.py

class Keys:

    @staticmethod
    def get_keys():
        k = Keys()
        return [k.__dict__[var] for var in k.__dict__]
