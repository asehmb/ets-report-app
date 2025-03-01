from flask import Flask, request, render_template, redirect, Blueprint, jsonify 
from database import Databases

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    """
    homepage
    """
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    bus_database = Databases()
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    result = 0;
    if data['value'] != "":
        print(bus_database.get_a_bus_stop(data['value']))
        bus_database.update_to_bus_database(data['value'], 1)
        result = bus_database.get_a_bus_stop(data['value'])
    return jsonify(result=result) # return the result to JavaScript


def save_to_bus_database():
    """
    purpose: saves to the bus stop database
    parameter: csv filename
    return: None
    """
    bus_database = Databases()
    bus_database.create_bus_stop_database()
    with open("ETS_Bus_Schedule_GTFS_Data_Feed_-_Stops_20250226.csv", 'r') as file:
        info = file.readlines()
        split_data = []
        for i in range(len(info)):
            split_data = info[i].strip().split(",")
            bus_database.push_to_bus_database(split_data[0], f"{split_data[4]} {split_data[5]}", 0)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
