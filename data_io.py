import numpy as np
import wfdb
import os
ERROR_MSG = """File extension {} is not supported.
               Please enter one of [txt]"""
def open_signal(file):
    extension = file.name.split('.')[-1]
    if extension == 'txt':
        return np.loadtxt(file)
    else:
        raise FileTypeNotSupportedError(extension)


class FileTypeNotSupportedError(Exception):
    def __init__(self, filetype, message=ERROR_MSG) -> None:
        self.message = message.format(filetype)
        super().__init__(self.message)