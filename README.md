# **Flipkart-Laptop-Data---Business-Insights-on-Product-Pricing**

## Overview

This project involves the development and deployment of a web application for predicting laptop prices based on various features such as brand, operating system, processor type, RAM size, RAM type, disk type, and disk size. The machine learning models used in the application include Linear Regression, Decision Tree Regression, Random Forest Regression, Gradient Boosting Regression, ADA Boost Regression, and XG Boost Regression.

## The project consists of three main components:

### Data Processing and Analysis: 
The dataset containing laptop details is loaded using the Pandas library. Features like brand, processor type, operating system, RAM size, RAM type, and storage are extracted and processed. Univariate and bivariate analysis is performed on the dataset using Matplotlib and Seaborn for insights into the data.

### Machine Learning Models: 
Various regression models such as Linear Regression, Decision Tree Regression, Random Forest Regression, Gradient Boosting Regression, ADA Boost Regression, and XG Boost Regression are trained and evaluated on the dataset to predict laptop prices. The models are then compared based on metrics like Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared score.

### Web Application Deployment: 
The predictive models are integrated into a Streamlit web application. Users can input laptop features such as brand, operating system, processor type, RAM size, RAM type, disk type, and disk size to get a predicted price. The application is deployed on Streamlit Cloud, making it accessible online.

## Project Structure
data: Folder containing the dataset (laptop_details.csv) used for training and analysis.

resourses: Folder containing the dataset and other resources.

app.py: Streamlit web application script that defines the user interface, takes user inputs, and uses the pre-trained models for predicting laptop prices.

model_training.ipynb: Jupyter Notebook containing the code for training the regression models. It includes data preprocessing, model creation, and evaluation.

pipe.pkl: Pickle file containing the serialized pre-trained models. This file is loaded in the Streamlit app for making predictions.

## Usage
Users can visit the deployed web application and input laptop features to receive a predicted price. The application offers a user-friendly interface for interacting with the machine learning models.

## Technologies Used
Python: The primary programming language for data processing, analysis, and web application development.

Pandas and NumPy: Libraries for data manipulation and analysis.

Matplotlib and Seaborn: Libraries for data visualization.

Scikit-learn: Library for machine learning models and preprocessing.

XGBoost: Gradient boosting library for regression.

Streamlit: Framework for building web applications.

Streamlit Cloud: Platform for deploying and hosting Streamlit applications online.

## Outcome
The deployed web application serves as a tool for users interested in predicting laptop prices based on various features. It provides a convenient and accessible interface for obtaining estimated prices, making it valuable for consumers and sellers in the laptop market.

