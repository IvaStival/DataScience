import streamlit as st
# import pandas as pd
# import numpy as np
#
# st.title("Streamlit Test")
#
# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data
#
# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(10000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Done! (using st.cache)")
#
# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)
#
# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#
# st.bar_chart(hist_values)
#
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)
def App1page():
    st.write("Showing app 1")

    if st.button("Return to Main Page"):
        st.session_state.runpage = main_page
        st.experimental_rerun()

def App2page():
    st.write("Showing app 2")
    if st.button("Return to Main Page"):
        st.session_state.runpage = main_page
        st.experimental_rerun()

def main_page():
    st.write("This is my main menu page")
    btn1 = st.button("Show App1")
    btn2 = st.button("Show App2")

    if btn1:
        st.session_state.runpage = App1page
        st.session_state.runpage()
        st.experimental_rerun()

    if btn2:
        st.session_state.runpage = App2page
        st.session_state.runpage()
        st.experimental_rerun()


if 'runpage' not in st.session_state:
    st.session_state.runpage = main_page
    st.session_state.runpage()
