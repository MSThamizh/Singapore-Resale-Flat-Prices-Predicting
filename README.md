# Singapore Flat Sale Price Prediction

This project aims to predict the resale prices of flats in Singapore, utilizing machine learning techniques to provide accurate pricing insights. The project leverages tools such as MongoDB Atlas for data storage, Streamlit for building an interactive application, and various visualization libraries to gain data insights.

## Problem Statement

The goal of this project is to develop a Streamlit application that allows users to explore and predict flat resale prices in Singapore effectively. Key features include:

- **Data Retrieval**: Manage and retrieve historical flat sale data from MongoDB Atlas.
- **Data Cleaning**: Handle missing values, remove duplicates, and convert data types for analysis.
- **Predictive Modeling**: Build regression models to predict flat resale prices based on location, flat type, floor area, and other features.
- **Prediction Visualization**: Enable users to visualize predicted prices based on their input features.

## Workflow

1. **Data Retrieval from MongoDB**: Fetch historical flat sales data from MongoDB Atlas, including features such as town, flat type, storey range, floor area, and lease commence date.
2. **Data Cleaning and Preparation**: Clean and preprocess the data to ensure it’s ready for modeling.
3. **Feature Engineering**: Apply transformations and scaling to optimize model performance.
4. **Model Building**: Train regression models to predict flat resale prices.
5. **Streamlit Web Application**: Develop an interactive web app that allows users to enter feature values and receive resale price predictions.

## Features

### 1. Data Understanding and Cleaning:
   - **Variable Identification**: Identifies and categorizes variables (categorical, numerical).
   - **Handling Missing Values**: Fills missing values with suitable techniques (e.g., mean or median for numerical data).
   - **Removing Duplicates**: Ensures that the dataset is free of duplicate entries.
   - **Type Conversion**: Converts data types as necessary to facilitate analysis and modeling.

### 2. Data Preprocessing:
   - **Missing Value Treatment**: Handles missing values using statistical methods (mean/median/mode).
   - **Outlier Management**: Uses IQR or Isolation Forest methods from scikit-learn to manage outliers.
   - **Skewness Correction**: Corrects skewness in continuous variables using log or Box-Cox transformations, especially for the target variable to improve model accuracy.
   - **Encoding Categorical Variables**: Applies one-hot, label, or ordinal encoding for categorical data.

### 3. Exploratory Data Analysis (EDA):
   - **Data Visualization**: Visualizes distributions, outliers, and skewness using Seaborn plots, including boxplots, distplots, and violin plots.
   - **Correlation Analysis**: Uses Seaborn’s heatmap to identify and remove highly correlated features.

### 4. Feature Engineering:
   - **Feature Creation**: Develops new features if applicable to enhance model inputs.
   - **Transformation and Scaling**: Applies transformations and scaling to ensure consistent data distribution and optimize model performance.

### 5. Model Building and Evaluation:
   - **Model Training**: Trains a regression model using cross-validation.
   - **Performance Evaluation**: Evaluates model performance with metrics such as RMSE, MAE, and R-squared.
   - **Hyperparameter Tuning**: Performs grid search and cross-validation to optimize model performance.

### 6. Streamlit Web Application:
   - **Interactive User Interface**: Provides an interactive application that allows users to enter feature values for prediction, except the target variable (resale price).
   - **Real-Time Predictions**: Implements feature engineering, scaling, and transformations in real-time to provide accurate predictions based on user input.

## Technologies Used

- **Python**: Main programming language for data processing and application development.
- **Streamlit**: Framework for building the interactive web application.
- **Scikit-learn**: For machine learning model development.
- **Pandas/Numpy**: For data manipulation and analysis.
- **Seaborn/Matplotlib**: For data visualization during EDA.

## References

- **Python**: [https://docs.python.org/3/](https://docs.python.org/3/)
- **Streamlit Documentation**: [https://docs.streamlit.io/library/api-reference](https://docs.streamlit.io/library/api-reference)
- **Scikit-learn Documentation**: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
- **Dataset**: [Data](https://docs.google.com/spreadsheets/d/18eR6DBe5TMWU9FnIewaGtsepDbV4BOyr/edit?usp=sharing&ouid=104970222914596366601&rtpof=true&sd=true)
