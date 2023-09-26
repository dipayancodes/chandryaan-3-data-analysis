import streamlit as st
import pandas as pd

data = pd.read_csv('data.csv')

st.title('Chandrayaan 3 Data Analysis')

options = ['Mission Details', 'Graphical Details']
selected_option = st.sidebar.selectbox('Select Data Option', options)

if selected_option == 'Mission Details':
    st.subheader('Mission Details:')
    st.dataframe(data, width=1000, height=400)  # Adjust width and height as needed

elif selected_option == 'Graphical Details':
    st.subheader('Mission Details Line Chart:')
    chart_data = data.set_index('Parameter')  # Set 'Parameter' column as the index
    st.line_chart(chart_data['Specifications'])  # Plot the 'Specifications' column as a line chart
