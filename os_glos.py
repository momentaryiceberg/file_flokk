import os

def make_dir():
    os.mkdir('ný_mappa')

def change_dir():
    os.chdir('/ný/slóð')

def current_dir():
    os.getcwd()

def remove_dir():
    os.rmdir('/eyda/þessum')

def rename_dir_or_file():
    os.rename('úr', 'í')

########################################################

def list_dir():
    """Return a list containing the names of the entries in the directory given by path"""
    os.listdir('/path')

def walk_tree():
    """Generate the file names in a directory tree by walking the tree either top-down or bottom-up."""
    #os.walk(top=[, topdown=True[, onerror=None[, followlinks=False]]])