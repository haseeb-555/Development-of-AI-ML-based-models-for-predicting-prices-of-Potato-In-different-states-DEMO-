Here is a possible implementation of an ARIMA model for predicting crop prices in a specific state using Flask, with future work including XGBoost, LSTM, and improved UI:

Crop Price Prediction using ARIMA Model and Flask

This project aims to predict the prices of potatoes in a specific state using an ARIMA (AutoRegressive Integrated Moving Average) model and deploy it using Flask.

Requirements

numpy
pandas
seaborn
matplotlib
scikit-learn
flask
Model Overview

The ARIMA model is a popular statistical model used for time series forecasting. It takes into account the auto-correlation, trend, and seasonality in the data to make accurate predictions. In this project, we have used the ARIMA model to predict the prices of potatoes in a specific state.

Dataset

The dataset used for training the model consists of historical potato prices in the specific state. The data is collected from reliable sources and preprocessed to ensure quality and consistency.

Model Training

The ARIMA model is trained on the preprocessed dataset using the statsmodels library in Python. The model is tuned using grid search to find the optimal parameters.

Model Deployment

The trained model is deployed using Flask, a micro web framework in Python. The Flask app takes in the input data and returns the predicted prices.

Future Work

Future work includes:

Training the model using XGBoost and other regression models: Introduce a new column which is the difference between the previous 2 days data and train the model using XGBoost and other regression models to improve the accuracy of the predictions.
Exploring LSTM concept: Explore the use of LSTM (Long Short-Term Memory) models for time series forecasting and compare its performance with the ARIMA model.
Improving the UI: Improve the user interface of the Flask app to make it more user-friendly and interactive.
