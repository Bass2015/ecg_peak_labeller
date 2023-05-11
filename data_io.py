import numpy as np
import io
import streamlit as st

ERROR_MSG = """File extension {} is not supported.
               Please enter one of [txt]"""
def open_signal(file):
    extension = file.name.split('.')[-1]
    if extension == 'txt':
        return np.loadtxt(file)
    else:
        raise ValueError(ERROR_MSG.format(extension))

def save_peaks(peaks:np.ndarray, format:str='txt'):
        
    if format == 'txt':
        with io.BytesIO() as buffer:
            np.savetxt(buffer, peaks, delimiter=",")
            st.download_button('Download', 
                            data=buffer,
                            file_name='peaks.txt'
                            )
        return buffer
    else:
        raise ValueError(ERROR_MSG.format(format))
