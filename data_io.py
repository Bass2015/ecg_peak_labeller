import numpy as np

ERROR_MSG = """File extension {} is not supported.
               Please enter one of [txt]"""
def open_signal(file):
    extension = file.name.split('.')[-1]
    if extension == 'txt':
        return np.loadtxt(file)
    else:
        raise ValueError(ERROR_MSG.format(extension))

