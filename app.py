from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)

# Load the SARIMAX model when the app starts
with open('model.pkl', 'rb') as f:
    sarimax_model = pickle.load(f)

with open('haryana1.pkl', 'rb') as f:
    up_model = pickle.load(f)

with open('uttarpradesh1.pkl', 'rb') as f:
    har_model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')  # Your landing page with form

@app.route('/predict', methods=['POST'])
def predict():
    state=request.form.get('state')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    
    # Print the dates to ensure they are captured correctly
    print(f"Start Date: {start_date}, End Date: {end_date}")
    
    # Generate the forecast steps and check if it's working
    forecast_steps = pd.date_range(start=start_date, end=end_date, freq='D')
    print(f"Forecast Steps: {forecast_steps}")
    if(state=='haryana'):
            # Forecast using the SARIMAX model
        print("haryana")
        forecast =har_model.get_forecast(steps=len(forecast_steps))

    
    # Debug output of the forecast
        forecast_mean = forecast.predicted_mean
        print(f"Forecast Mean: {forecast_mean}")
    
        forecast_conf_int = forecast.conf_int()
        forecast_df = pd.DataFrame({
            'Forecast': forecast_mean,
            'Lower CI': forecast_conf_int.iloc[:, 0],
            'Upper CI': forecast_conf_int.iloc[:, 1]
        }, index=forecast_steps)


    elif(state=='uttarpradesh'):
            # Forecast using the SARIMAX model
        print("uttarpradesh")
        forecast =up_model.get_forecast(steps=len(forecast_steps))
    
    # Debug output of the forecast
        forecast_mean = forecast.predicted_mean
        print(f"Forecast Mean: {forecast_mean}")
    
        forecast_conf_int = forecast.conf_int()
        forecast_df = pd.DataFrame({
            'Forecast': forecast_mean,
            'Lower CI': forecast_conf_int.iloc[:, 0],
            'Upper CI': forecast_conf_int.iloc[:, 1]
        }, index=forecast_steps)

        

    # Render the results to the prediction.html template
    return render_template('prediction.html', forecast=forecast_df)


if __name__ == '__main__':
    app.run(debug=True)
