import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
file_path = r"C:\Users\dhrub\Downloads\prodigy ds dataset\TASK2\train.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand its structure
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Step 2: Data Cleaning
# Fill missing values in numeric columns with their respective medians
numeric_cols = ['Age', 'Fare']  # Specify numeric columns here
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

# Drop any remaining rows with missing values (if necessary)
df.dropna(inplace=True)

# Confirm no missing values remain
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 3: Exploratory Data Analysis (EDA)
# Display basic statistics of numeric columns
print("\nDataset Summary:")
print(df.describe())

# Display information about the dataset
print("\nDataset Information:")
print(df.info())

# Step 4: Visualization and EDA

# Countplot of Survived
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', data=df)
plt.title('Distribution of Survived')
plt.show()

# Countplot of Survived by Sex
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', hue='Sex', data=df)
plt.title('Survival by Sex')
plt.show()

# Countplot of Survived by Pclass
plt.figure(figsize=(6, 4))
sns.countplot(x='Survived', hue='Pclass', data=df)
plt.title('Survival by Pclass')
plt.show()

# Age Distribution (handle categorical variables)
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Correlation heatmap (only numeric columns)
numeric_df = df.select_dtypes(include=['number'])
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
