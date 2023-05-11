import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import data_io
import wfdb
from streamlit_plotly_events import plotly_events
import io

def plot_signal(signal):
    """Makes the plotly Figure to display a signal. 
    Has subplot that will display the selected peaks"""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(len(signal)), 
                             y= signal, 
                             line={'width':0.9, 'color':'blue'}, 
                             name='ECG signal'))
    peaks = st.session_state.get('peaks', [])
    fig.add_trace(go.Scatter(x=peaks, 
                             y= signal[peaks], 
                             mode='markers', 
                             opacity=0.5,
                             marker={
                                 'size': 12,
                                 'line': {'width':2, 'color':'red'},
                                 'color':'white',
                             }, 
                             name='Labeled peak'))
    fig.update_layout(hovermode='closest')
    return fig

# Will have to delete
# def save_peaks(peaks):
    # record = st.session_state.selected_record
    # st.session_state['records_df'].at[record, 'peaks'] = peaks
    # st.session_state['records_df'].at[record, 'labeled'] = True
    # st.session_state['records_df'].to_pickle('records_df.pkl')

def capture_click(figure):
    """Adds the click event listener to the figure. 
    This listener will append any clicked point to the current
    list of peaks."""
    st.session_state['peaks'] = st.session_state.get('peaks', [])
    selected_point = plotly_events(figure, override_width=1000, click_event=True)
    if len(selected_point) != 0:
        st.session_state['peaks'].append(selected_point[0]['x'])
        st.session_state['peaks'].sort()
        st.experimental_rerun()


def peak_selection_form(col):
    """Shows the selected peaks. The button calls a method to save
    the list"""
    with st.form('Peaks_form'):
        peak_idx = st.text_area("Peak indeces", 
                                st.session_state['peaks'], 
                                disabled=True)
        
        if len(st.session_state['peaks']) > 0:
            peak_array = np.asarray(st.session_state['peaks'])
            
        st.form_submit_button('Save', on_click=data_io.save_peaks, kwargs={'peaks':peak_array if len(st.session_state['peaks']) > 0 else None})

def clear_peaks():
    peaks = st.session_state.get('peaks', None)
    if peaks == None:
        return
    peaks.clear()

def header_line():
    col1, col2, col3 = st.columns([3, 5, 2])
    file = col1.file_uploader("Upload file")
    if file is not None:
        try:
            st.session_state['signal'] = data_io.open_signal(file)
        except Exception as err:
            st.warning(err)
    col3.button('Clear peaks', on_click=clear_peaks)
    return col2

if __name__ == '__main__':
    st.set_page_config(layout='wide')
    col = header_line()
    st.session_state['signal'] = st.session_state.get('signal',
                                  np.loadtxt('example_signal.txt') )
    plot = plot_signal(st.session_state['signal'])
    capture_click(plot)
    peak_selection_form(col)
    

