import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events

st.set_page_config(layout='wide')

# Temporal, later will accept any kind of data
def get_ecg_signal(filepath):
    ecg_data = pd.read_csv(filepath)
    ecg_data = ecg_data[9:] \
                    .rename(columns={'Name' : 'unit', 
                                    'Emil jimenez' : 'decimal'}) \
                    .reset_index()
    return (ecg_data['unit'] + '.' + ecg_data['decimal']).astype(float)

def plot_signal(signal):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(len(signal)), y= signal, line={'width':0.9, 'color':'blue'}))
    peaks = st.session_state.get('peaks', [])
    fig.add_trace(go.Scatter(x=peaks, 
                             y= signal[peaks], 
                             mode='markers', 
                             opacity=0.5,
                             marker={
                                 'size': 12,
                                 'line': {'width':2, 'color':'red'},
                                 'color':'white',
                             }))
    fig.update_layout(hovermode='closest')
    return fig

def save_peaks(peaks, filename):
    with open(filename, 'w') as f:
        f.write(str(peaks)[1:-1])
    st.session_state['peaks'].clear()

def capture_click(plot):
    st.session_state['peaks'] = st.session_state.get('peaks', [])
    selected_point = plotly_events(plot, override_width=1000, click_event=True)
    if len(selected_point) != 0:
        st.session_state['peaks'].append(selected_point[0]['x'])
    st.session_state['peaks'].sort()

def peak_selection_form(save_peaks):
    with st.form('Peak selection', clear_on_submit=True):
        peak_idx = st.multiselect('Peak indeces', 
                st.session_state['peaks'], 
                default=st.session_state['peaks'],
                key='peak_multiselect')

        st.form_submit_button('Save', on_click=save_peaks, args=(peak_idx, 'ecg_PL/Peaks.txt'))

signal = get_ecg_signal('electrocardiograms/ecg_2023-01-21_1.csv')
plot = plot_signal(signal)
capture_click(plot)
peak_selection_form(save_peaks)

