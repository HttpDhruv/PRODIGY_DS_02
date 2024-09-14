Survival Data Analyzer

This project focuses on cleaning, exploring, and visualizing a dataset related to survival data, likely from a Titanic-like dataset. The script performs data cleaning, exploratory data analysis (EDA), and visualizes various aspects of the data to uncover insights into survival rates based on features such as age, sex, and passenger class.

Features:
Data Loading: Loads a dataset from a CSV file.
Data Cleaning:
Handles missing values in numeric columns (Age, Fare) by filling them with the median.
Drops any remaining rows with missing values.
Exploratory Data Analysis (EDA):
Provides a summary of the dataset, including basic statistics and data information.
Visualization:
Count Plot of Survival: Shows the distribution of survival status.
Count Plot of Survival by Sex: Visualizes survival rates by gender.
Count Plot of Survival by Pclass: Shows survival rates by passenger class.
Age Distribution: Displays the distribution of passenger ages with a histogram.
Correlation Heatmap: Provides a heatmap of correlations between numeric features.


Prerequisites:
Python 3.x

Required Libraries:
pandas
matplotlib
seaborn
