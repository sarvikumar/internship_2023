# Importing required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)
# Setting up the app
st.set_page_config(page_title="Data Visualization Dashboard", layout="wide")

# Loading the dataset
df = pd.read_csv("D:\innomatics\Titanic.csv")

# Cleaning and preprocessing the data
df.dropna(inplace=True)

# Adding widgets for user interaction
st.sidebar.title("Data Visualization Dashboard")
plot_type = st.sidebar.selectbox("Select Plot Type", ["Histogram", "Scatter Plot", "Box Plot"])

# Creating data visualizations based on user selection
if plot_type == "Histogram":
    st.header("Histogram")
    sns.histplot(df['Age'], kde=True)
    st.pyplot()
elif plot_type == "Scatter Plot":
    st.header("Scatter Plot")
    sns.scatterplot(x='Age', y='Fare', data=df, hue='Sex')
    st.pyplot()
elif plot_type == "Box Plot":
    st.header("Box Plot")
    sns.boxplot(x='Pclass', y='Age', data=df, hue='Sex')
    st.pyplot()
