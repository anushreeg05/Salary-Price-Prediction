# Salary Prediction App

This project is a simple **Salary Prediction App** that uses **Linear Regression** to predict the salary of an individual based on their years of experience. The app is developed using **Python** and **Streamlit** for the front-end interface.

## Table of Contents
- [Project Overview]
- [Dataset]
- [Installation]
- [How to Use]
- [Model Evaluation]
- [Technologies Used]
- [Future Enhancements]

## Project Overview
The purpose of this project is to build a machine learning model using **Linear Regression** to predict salaries based on years of experience. The user can input the number of years of experience, and the model will predict the corresponding expected salary. This app is built with **Streamlit** to create an interactive and user-friendly interface.

## Dataset
The project uses a dataset `Salary Data.csv` which contains information such as:
- Age
- Gender
- Education Level
- Job Title
- Years of Experience
- Salary

The dataset is pre-processed to handle missing values, and Linear Regression is applied to predict salary based on the years of experience.

## Installation

1. Clone the repository to your local machine.
   ```bash
   git clone <repository-link>

2. Install the required dependencies.
   pip install -r requirements.txt

3. Ensure that you have Streamlit installed:
   pip install streamlit

4. Make sure the dataset Salary Data.csv is in the correct path:
   C:/Users/anush/Desktop/PROJECT/Salary Data.csv


## How to Use
1. Train the model:

The model is trained using the LinearRegression class from scikit-learn.
Missing values in the dataset are handled by filling them with mean values or forward-filling for categorical variables.

2. Run the Streamlit app:
   streamlit run app.py

3. The app will prompt you to input the number of years of experience, and on clicking the Predict button, it will display the predicted salary.

4. For local deployment and testing, the app can also be accessed on a local tunnel using the command:
   npx localtunnel --port 8501

## Model Evaluation
The performance of the linear regression model is evaluated using the following metrics:

- Mean Squared Error (MSE): Measures the average of the squares of the errors.
- Mean Absolute Error (MAE): Represents the average of the absolute differences between predicted and actual values.
- Root Mean Squared Error (RMSE): The square root of the mean squared error, which penalizes large errors.
- R² Score: Indicates the proportion of the variance in the dependent variable that is predictable from the independent variable.

## Technologies Used

- Python: The core programming language.
- NumPy: For numerical operations.
- Pandas: For data manipulation and analysis.
- Matplotlib: For visualizing the data.
- Scikit-learn: For implementing the linear regression model.
- Streamlit: For building the web application.
- Joblib: For saving and loading the model.

## Future Enhancements

- Improve the user interface with additional input fields and more aesthetic design.
- Explore other machine learning algorithms to compare and potentially improve the accuracy of the model.
- Add a feature for users to upload their own dataset and receive predictions based on their data.
