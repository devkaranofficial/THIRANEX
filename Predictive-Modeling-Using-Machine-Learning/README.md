# House Price Prediction Using Linear Regression

## Project Overview

This project demonstrates the implementation of a Machine Learning model for predicting house prices using Linear Regression. The model is trained on the Ames Housing Dataset from Kaggle and uses multiple property-related features to estimate the sale price of a house.

The objective of this project is to gain practical experience in supervised machine learning, data preprocessing, model training, evaluation, visualization, and predictive analysis.

## Features

* Data preprocessing and feature selection
* Linear Regression model implementation
* Train-test data splitting
* House price prediction
* Model performance evaluation
* Data visualization using Matplotlib
* Model saving using Pickle
* Future house price prediction

## Dataset

Dataset Source:

Kaggle House Prices - Advanced Regression Techniques

The dataset contains information about residential homes and their sale prices.

### Features Used

* GrLivArea (Above Ground Living Area)
* BedroomAbvGr (Number of Bedrooms)
* FullBath (Number of Full Bathrooms)
* GarageCars (Garage Capacity)
* GarageArea (Garage Area)
* OverallQual (Overall Material and Finish Quality)
* YearBuilt (Construction Year)
* TotalBsmtSF (Total Basement Area)

### Target Variable

* SalePrice

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Pickle

## Project Structure

```text
House-Price-Prediction/
│
├── Predictive_Modeling_Using_Machine_Learning.py
├── train.csv
├── house_price_model.pkl
├── screenshots/
│   ├── actual_vs_predicted.png
│   ├── residual_plot.png
│   └── terminal_output.png
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
```

Navigate to the project folder:

```bash
cd House-Price-Prediction
```

Install required libraries:

```bash
pip install pandas numpy matplotlib scikit-learn
```

## Running the Project

Execute the Python script:

```bash
python Predictive_Modeling_Using_Machine_Learning.py
```

The script will:

* Load the dataset
* Train the Linear Regression model
* Generate predictions
* Evaluate model performance
* Display graphs
* Save the trained model

## Evaluation Metrics

The model is evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Mean Absolute Percentage Error (MAPE)
* R² Score

## Visualizations

### Actual vs Predicted House Prices

This graph compares actual house prices with predicted house prices.

### Residual Plot

The residual plot helps analyze prediction errors and model performance.

### Feature Correlation Analysis

Shows how strongly each feature is related to house sale prices.

## Sample Output

```text
MODEL PERFORMANCE

MAE   : 28,000.00
MSE   : 1,850,000,000.00
RMSE  : 43,000.00
R²    : 0.78
MAPE  : 0.15
Accuracy (R²%) : 78%
```

## Future Improvements

* Random Forest Regression
* XGBoost Regression
* Hyperparameter Tuning
* Feature Engineering
* Web Application Deployment using Flask or Streamlit

## Learning Outcomes

Through this project, I learned:

* Data preprocessing techniques
* Feature selection
* Linear Regression implementation
* Model evaluation methods
* Data visualization
* Machine Learning workflow

## Author

Dev Karan Singh

Internship Project – Predictive Modeling Using Machine Learning
