Survival Data Explorer


This project is focused on cleaning, exploring, and visualizing a dataset containing survival data. The dataset is processed using Python, and key insights are visualized using count plots, histograms, and correlation heatmaps. The project employs data cleaning techniques and exploratory data analysis (EDA) to uncover relationships between features and survival rates.

Features
Data Loading: Loads a dataset from a CSV file for analysis.
Data Cleaning: Handles missing values by filling numeric columns (Age, Fare) with the median and dropping any remaining rows with missing values.
Exploratory Data Analysis (EDA):
Provides summary statistics and detailed information about the dataset.
Visualizes relationships between survival and key features such as gender, class, and age.
Visualization:
Count plots for survival distribution by sex and class.
Histograms for age distribution.
Correlation heatmap to understand relationships between numeric variables.


Prerequisites
Python 3.x

Required Libraries:
pandas
matplotlib
seaborn
