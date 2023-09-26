import streamlit as st
import pandas as pd

# Load your Chandrayaan data (replace 'data.csv' with your data file)
data = pd.read_csv('data.csv')

# Set the title of your Streamlit app
st.title('Chandrayaan 3 Data Analysis')

# Create a sidebar where users can select data options
options = ['Mission Details', 'Graphical Details']
selected_option = st.sidebar.selectbox('Select Data Option', options)

if selected_option == 'Mission Details':
    # Display data table for mission details
    st.subheader('Mission Details:')
    st.dataframe(data, width=1000, height=400)  # Adjust width and height as needed

elif selected_option == 'Graphical Details':
    # Create a line chart for mission details using st.line_chart
    st.subheader('Mission Details Line Chart:')
    chart_data = data.set_index('Parameter')  # Set 'Parameter' column as the index
    st.line_chart(chart_data['Specifications'])  # Plot the 'Specifications' column as a line chart
