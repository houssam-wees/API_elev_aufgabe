from flask import Flask, request, jsonify
import pandas as pd
from dateutil import parser

app = Flask(__name__)

# Load and process the data
csv_data = pd.read_csv('/Users/houssam/Downloads/Fahrtdaten.csv')
csv_data['ts'] = pd.to_datetime(csv_data['ts'], unit='ms')
csv_data['date'] = csv_data['ts'].dt.date

@app.route('/rides_per_day', methods=['GET'])
def get_rides_per_day():
    date_start = request.args.get('date_start')
    date_end = request.args.get('date_end')

    # chack that dates are provided
    if not date_start or not date_end:
        return "start and end dates are not speciied, please give specific dates", 400

    try:
        start_date = parser.parse(date_start).date()
        end_date = parser.parse(date_end).date()
    except ValueError:
        return {"error: Invalid date format"}, 400

    # giving results  between two specific dates
    date_range = csv_data[(csv_data['date'] >= start_date) & (csv_data['date'] <= end_date)]

    # Aggregate data
    rides_per_day = date_range.groupby('date').size()
    max_num_of_rides = max(rides_per_day)   
    rides_per_day = {str(date): count for date, count in rides_per_day.items()}
    

    return {"rides_per_day": rides_per_day, "max_num_of_rides":max_num_of_rides}

    # finding the day with the most travels
    

if __name__ == '__main__':
    app.run(port=12345)
