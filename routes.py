
from flask import render_template, request
from server import app
from src.request import get_station_occupancy_data



@app.route('/', methods=['POST', 'GET'])
def homepage():

    data = request.form
    if request.method == 'POST':
        station_name = data.get('Station').lower()
        if station_name == '':
            return render_template('index.html', errorMsg = "Station Input Empty")
        elif station_name != 'ashfield' and station_name != 'kogarah' and station_name != 'seven hills' and station_name != 'manly vale':
            return render_template('index.html', errorMsg = "Station input is not valid, read the small text")
        else:
            station_occupancy = get_station_occupancy_data(station_name)
            return render_template('index.html', parking_data=station_occupancy)


    return render_template('index.html')