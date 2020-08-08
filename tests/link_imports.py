#link_imports.py

import os,sys,inspect

def link_parent_directory():
    currentdir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir=os.path.dirname(currentdir)
    sys.path.insert(0,parentdir)
