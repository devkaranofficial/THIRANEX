# Student Performance Analysis

## Project Overview

This project was developed as part of the Thiranex Data Science Internship.

The objective of this project is to perform data cleaning, preprocessing, visualization, and exploratory data analysis (EDA) on a student performance dataset using Python.

The project demonstrates the complete data analysis workflow from raw data preparation to extracting meaningful insights through visualizations.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Dataset Information

The dataset contains academic information for 1000 students, including:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

---

## Data Cleaning Process

### Missing Values

Checked the dataset for missing values.

Result:

- No missing values found.

### Duplicate Records

Checked for duplicate records.

Result:

- No duplicate records found.

### Outlier Detection

Used the Interquartile Range (IQR) method to identify and remove outliers from the Average Score column.

Results:

- Original Records: 1000
- Final Records: 994
- Outliers Removed: 6

---

## Feature Engineering

Created two new features:

### Average Score

Calculated using:

```python
average_score = (
    math_score +
    reading_score +
    writing_score
) / 3
```

### Performance Category

Students were categorized into:

- Excellent
- Good
- Average
- Poor

---

## Visualizations Generated

### 1. Score Distribution

Displays the distribution of student average scores.

### 2. Gender Performance Analysis

Compares average scores between male and female students.

### 3. Test Preparation Impact

Shows how completing a test preparation course affects academic performance.

### 4. Performance Categories

Visualizes student distribution across performance groups.

### 5. Correlation Heatmap

Illustrates relationships among academic subjects.

### 6. Dashboard

Combines key visualizations into a single analytical dashboard.

---

## Key Findings

### Test Preparation Improves Performance

Students who completed the test preparation course achieved significantly higher average scores.

### Female Students Performed Better

Female students showed slightly higher median academic performance.

### Strong Correlation Between Reading and Writing

Reading and writing scores exhibited a strong positive correlation.

### Majority of Students Performed Well

Most students belonged to the Good performance category.

### Data Cleaning Improved Quality

Outlier treatment enhanced overall dataset reliability.

---

## Project Structure

```text
THIRANEX
│
├── student_performance_analysis.py
├── StudentsPerformance.csv
├── cleaned_student_performance.csv
├── requirements.txt
│
├── score_distribution.png
├── gender_performance.png
├── test_preparation_impact.png
├── performance_categories.png
├── correlation_heatmap.png
└── student_dashboard.png
```

---

## How To Run

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

Run:

```bash
python student_performance_analysis.py
```

---

## Author

Dev Karan Singh

Data Science Intern

Thiranex
