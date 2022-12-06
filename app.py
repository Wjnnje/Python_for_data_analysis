from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def hello():
	return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
	hour = int(request.form['hour'])
	temperature = float(request.form['temperature'])
	humidity = float(request.form['humidity'])
	wind_speed = float(request.form['wind_speed'])
	visibility = float(request.form['visibility'])
	solar_radiation = float(request.form['solar_radiation'])
	rainfall = float(request.form['rainfall'])
	snowfall = float(request.form['snowfall'])
	holiday = int(request.form['holiday'])
	day = int(request.form['day'])
	month = int(request.form['month'])
	
	prediction = model.predict([[hour, temperature, humidity, wind_speed, visibility, solar_radiation, rainfall, snowfall, holiday, day, month]])
	output =  int(prediction) if prediction >=0 else 0
	#output = round(prediction[0], 2)
	return render_template('index.html', prediction_text=f'Number of rented bikes: {output}')

if __name__ == "__main__":
	app.run()