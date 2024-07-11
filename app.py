from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Dict
import pandas as pd
from dateutil import parser
from datetime import date
import uvicorn


# Loading and processing csv data
elev_data = pd.read_csv('./Fahrtdaten.csv')
elev_data['ts'] = pd.to_datetime(elev_data['ts'], unit='ms')
elev_data['date'] = elev_data['ts'].dt.date


app = FastAPI()

class RidesPerDayResponse(BaseModel):
    rides_per_day: Dict[str, int]

# this only to have root on the api and through any errors   
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/rides_per_day", response_model=RidesPerDayResponse)
def get_rides_per_day(date_start: str = Query(...), date_end: str = Query(...)) -> dict:
    try:
        # here I am using the parser to get starting and ending dates
        start_date = parser.parse(date_start).date()
        end_date = parser.parse(date_end).date()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")
    try:
        # here I am filtering the query
        elev_data_range = elev_data[(elev_data['date'] >= start_date) & (elev_data['date'] <= end_date)]

        # here I groupped the data by data and took the size of that 
        rides_per_day = elev_data_range.groupby('date').size()
        rides_per_day_dict = {str(date_index):count for date_index, count in rides_per_day.items()}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    


    return {"rides_per_day": rides_per_day_dict}
    

#f __name__ == '__main__':
   
 #   uvicorn.run(app, host="127.0.0.1", port=12345)
