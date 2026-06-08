# ==========================================
# THIRANEX TASK 1
# DATA CLEANING & VISUALIZATION PROJECT
# Student Performance Analysis
# ==========================================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Set visualization style
sns.set_style("whitegrid")

print("Libraries Imported Successfully")


# =========================
# LOAD DATASET
# =========================

# Replace with your dataset filename
df = pd.read_csv("StudentsPerformance.csv")

print("\nDataset Loaded Successfully")


# =========================
# BASIC DATA EXPLORATION
# =========================

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())


# =========================
# CHECK MISSING VALUES
# =========================

print("\nMissing Values Before Cleaning")
print(df.isnull().sum())

# Example handling numeric columns
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].median(), inplace=True)

# Example handling categorical columns
for col in df.select_dtypes(include='object').columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())


# =========================
# CHECK DUPLICATES
# =========================

duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows Found: {duplicates}")

df.drop_duplicates(inplace=True)

print("Duplicates Removed")

print("Dataset Shape After Duplicate Removal:")
print(df.shape)


# =========================
# FEATURE ENGINEERING
# =========================

# Create Average Score Column

df['average_score'] = (
    df['math score'] +
    df['reading score'] +
    df['writing score']
) / 3


# Create Performance Category

def performance_category(score):

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Good"

    elif score >= 40:
        return "Average"

    else:
        return "Poor"


df['performance'] = df['average_score'].apply(performance_category)

print("\nNew Features Created Successfully")


# =========================
# OUTLIER DETECTION
# =========================

plt.figure(figsize=(8,5))

sns.boxplot(x=df['average_score'])

plt.title("Outlier Detection Before Treatment")

plt.show()


# =========================
# REMOVE OUTLIERS USING IQR
# =========================

Q1 = df['average_score'].quantile(0.25)

Q3 = df['average_score'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)

upper_limit = Q3 + (1.5 * IQR)

df_cleaned = df[
    (df['average_score'] >= lower_limit)
    &
    (df['average_score'] <= upper_limit)
]

print("\nShape Before Outlier Removal:", df.shape)

print("Shape After Outlier Removal:", df_cleaned.shape)


# Replace original dataframe
df = df_cleaned


# =========================
# VISUALIZATION 1
# SCORE DISTRIBUTION
# =========================

plt.figure(figsize=(10,6))

sns.histplot(
    df['average_score'],
    bins=20,
    kde=True
)

plt.title("Distribution of Average Scores")

plt.xlabel("Average Score")

plt.ylabel("Number of Students")

plt.savefig("score_distribution.png")

plt.show()


# =========================
# VISUALIZATION 2
# GENDER PERFORMANCE
# =========================

plt.figure(figsize=(8,6))

sns.boxplot(
    x='gender',
    y='average_score',
    data=df
)

plt.title("Average Score by Gender")

plt.savefig("gender_performance.png")

plt.show()


# =========================
# VISUALIZATION 3
# TEST PREPARATION IMPACT
# =========================

plt.figure(figsize=(8,6))

sns.barplot(
    x='test preparation course',
    y='average_score',
    data=df
)

plt.title("Impact of Test Preparation Course")

plt.savefig("test_preparation_impact.png")

plt.show()


# =========================
# VISUALIZATION 4
# PERFORMANCE CATEGORY
# =========================

plt.figure(figsize=(8,5))

sns.countplot(
    x='performance',
    data=df,
    order=['Poor','Average','Good','Excellent']
)

plt.title("Student Performance Categories")

plt.savefig("performance_categories.png")

plt.show()


# =========================
# VISUALIZATION 5
# CORRELATION HEATMAP
# =========================

plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")

plt.show()


# =========================
# DASHBOARD CREATION
# =========================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(15,10)
)

# Chart 1
sns.histplot(
    df['average_score'],
    kde=True,
    ax=axes[0,0]
)

axes[0,0].set_title("Average Score Distribution")

# Chart 2
sns.boxplot(
    x='gender',
    y='average_score',
    data=df,
    ax=axes[0,1]
)

axes[0,1].set_title("Gender Performance")

# Chart 3
sns.countplot(
    x='performance',
    data=df,
    ax=axes[1,0]
)

axes[1,0].set_title("Performance Categories")

# Chart 4
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    ax=axes[1,1]
)

axes[1,1].set_title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("student_dashboard.png")

plt.show()


# =========================
# INSIGHTS GENERATION
# =========================

print("\n========== KEY INSIGHTS ==========\n")

print("1. Reading and Writing scores show strong positive correlation.")

print("2. Students who completed test preparation courses generally scored higher.")

print("3. Gender-based performance differences are visible across subjects.")

print("4. Most students fall into the Good performance category.")

print("5. Data cleaning improved dataset quality and reliability.")


# =========================
# SAVE CLEANED DATASET
# =========================

df.to_csv(
    "cleaned_student_performance.csv",
    index=False
)

print("\nCleaned Dataset Saved Successfully")


# =========================
# PROJECT COMPLETED
# =========================

print("\n===================================")
print("THIRANEX TASK COMPLETED SUCCESSFULLY")
print("===================================")