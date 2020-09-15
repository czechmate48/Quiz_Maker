# link_imports.py

import os
import sys
import inspect

def link_parent_directory():
    currentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentDir = os.path.dirname(currentDir)
    sys.path.insert(0, parentDir)
