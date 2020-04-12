# ==================================
# IMPORT ALL RELEVANT MODULES
# ==================================

import numpy as np
import pandas as pd
from scipy import stats
from scipy import mean
from datetime import datetime 
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


from flask import Flask, jsonify



# ===========================================================
# CREATE AN ENGINE TO CONNECT TO THE SQLITE DATABASE
# ===========================================================

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)



# ===========================================================
# EXPLORE THE DATABASE "HAWAII.SQLITE" TO GET THE TABLES
# ===========================================================

inspector = inspect(engine)
tables = inspector.get_table_names()
print(tables)



# ===========================================================
# REFLECT THE DATABASE "HAWAII.SQLITE" INTO AN ORM MODEL
# ===========================================================

Base = automap_base()
Base.prepare(engine, reflect=True)



# ===========================================================
# VIEW THE CLASSES FOUND BY AUTOMAP
# ===========================================================

print(Base.classes.keys())



# ===========================================================
# SAVE REFERENCES TO EACH DATABASE TABLE
# ===========================================================

Measurement = Base.classes.measurement
Station = Base.classes.station



# ===========================================================
# FLASK - DEFINE THE APP
# ===========================================================

app = Flask(__name__)


# ===========================================================
# HOME PAGE
# Home page -- List all routes that are available.
# ===========================================================

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        "Hawaii Precipitation and Weather Data<br/><br/>"
        "Please select from the available routes below:<br/><br/>"
        "The Precipitation levels from 2016-08-23 to 2017-08-23.<br/>"
        "/api/v1.0/precipitation<br/><br/>"
        "A list of all the weather stations.<br/>"
        "/api/v1.0/stations<br/><br/>"
        "The Temperature Observations from 2016-08-23 to 2017-08-23.<br/>"
        "/api/v1.0/tobs<br/><br/>"
        "Please type in a start date (e.g. api/v1.0/temp/2016-01-01) to see the min, max and avg temperature from that start date till 08/23/2017.<br/>"
        "/api/v1.0/temp_from_start_date/<start><br/><br/>"
        "Please type in a date range (e.g. api/v1.0/temp/2016-01-01/2016-12-31) to see the min, max and avg temperature for that date range.<br/>"
        "/api/v1.0/temp_date_range/<start>/<end><br/>"
    )



# ==========================================================================================
# API - PRECIPITATION DATA FOR THE LAST 12 MONTHS
# /api/v1.0/precipitation
# Query for the dates and precipitation observations for the last 12 months in the dataset.
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
# ==========================================================================================

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Query for the dates and precipitation observations for the last 12 months in the dataset.
    Convert the query results to a Dictionary using date as the 'key 'and 'prcp' as the value.
    Return the JSON representation of your dictionary"""

    # Start a session to query the database
    session = Session(engine)

    # Retrieve the last 12 months of precipitation data
    date_latest_v1 = '2017-08-23'
    date_latest_formatted_v1 = datetime.strptime(date_latest_v1, '%Y-%m-%d')
    one_year_ago_v1 = date_latest_formatted_v1 - relativedelta(years=1)
    one_year_ago_minus_one_day_v1 = one_year_ago_v1 - relativedelta(days=1)

    results_last_year_prcp = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > one_year_ago_minus_one_day_v1).\
        order_by(Measurement.date).all()

    # Create a dictionary from the returned results and append to a list called "precipitation_data"
    precipitation_data = []
    for i in results_last_year_prcp:
        prcp_data_dict = {}
        prcp_data_dict["Date"] = i.date
        prcp_data_dict["Precipitation"] = i.prcp
        precipitation_data.append(prcp_data_dict)
   
    # Close the session
    session.close

    # Return a JSON list of dates and precipitation observations for the last 12 months in the dataset.
    return jsonify(precipitation_data)



# ===========================================================
# API - LIST OF ALL STATIONS
# /api/v1.0/stations
# Return a JSON list of stations from the dataset.
# ===========================================================

@app.route("/api/v1.0/stations")
def stations():
    """Return a json list of stations from the dataset."""
    
    # Start a session to query the database
    session = Session(engine)

    # Retrieve all the stations
    results_all_stations = session.query(Station).all()

    # Create a dictionary from the returned results and append to a list called "list_of_all_stations".
    list_of_all_stations = []
    for i in results_all_stations:
        stations_dict = {}
        stations_dict["Station"] = i.station
        stations_dict["Station Name"] = i.name
        stations_dict["Latitude"] = i.latitude
        stations_dict["Longitude"] = i.longitude
        stations_dict["Elevation"] = i.elevation
        list_of_all_stations.append(stations_dict)
    
    # Close the session
    session.close

    # Return a JSON list of stations from the dataset.
    return jsonify(list_of_all_stations)



# ====================================================================================================
# API - OBSERVED TEMPERATURES FOR THE LAST 12 MONTHS FOR THE MOST ACTIVE STATION
# /api/v1.0/tobs
# Query the dates and temperature observations of the most active station for the last year of data
# Return a JSON list of temperature observations (TOBS) for the previous year
# ====================================================================================================

@app.route("/api/v1.0/tobs")
def tobs():
    """Query the dates and temperature observations of the most active station for the last year of data.
    Return a json list of Temperature Observations (tobs) for the previous year"""
      
    # Start a session to query the database
    session = Session(engine)

    # Retrieve the last 12 months of temperature data for the most active station
    date_latest_v2 = '2017-08-23'
    date_latest_formatted_v2 = datetime.strptime(date_latest_v2, '%Y-%m-%d')
    one_year_ago_v2 = date_latest_formatted_v2 - relativedelta(years=1)
    one_year_ago_minus_one_day_v2 = one_year_ago_v2 - relativedelta(days=1)

    results_last_year_tobs_most_active_st = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date > one_year_ago_minus_one_day_v2).\
        filter(Measurement.station == 'USC00519281').all()
                            
    # Create a dictionary from the returned results and append to a list called "temp_data" 
    temp_data = []
    for i in results_last_year_tobs_most_active_st:
        tobs_data_dict = {}
        tobs_data_dict["Date"] = i.date
        tobs_data_dict["Temperature"] = i.tobs
        temp_data.append(tobs_data_dict)
    
    # Close the session
    session.close

    # Return a JSON list of temperature observations (TOBS) for the previous year
    return jsonify(temp_data)



# ============================================================================================
# API - CALCULATE MIN, AVG, MAX TEMP FOR ALL DATES GREATER THAN AND EQUAL TO THE PROVIDED START DATE
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature
# When given the start date only, calculate TMIN, TAVG, and TMAX for all dates 
# greater than and equal to the start date.
# =============================================================================================

@app.route("/api/v1.0/temp_from_start_date/<start>")
def start_stats(start=None):
    """Return a json list of the minimum temperature, the average temperature, and the max temperature. 
    When given the start date only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date"""

    # Start a session to query the database
    session = Session(engine)
        
    # Format the specified start date
    import datetime as dt
    start_date_only = start
    start_date_only_formatted = dt.datetime.strptime(start_date_only, '%Y-%m-%d')
    
    # Specify the last date in the dataset and format it
    max_date = '2017-08-23'
    max_date_formatted = dt.datetime.strptime(max_date, '%Y-%m-%d')

    # Create a function that calculates the "daily normals" 
    # This function calculates the minimum, average and maximum temperature for a specified date
    def daily_normals(date):
        """Daily Normals.
        Args:
        date (str): A date string in the format '%Y-%m-%d'
        Returns:
        A list of tuples containing the daily normals, tmin, tavg, and tmax
        """
    
        sel = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
        return session.query(*sel).filter(func.strftime('%Y-%m-%d', Measurement.date) == date).all()

    # Create a list to contain the dates
    specified_start_date = []

    # Create a list to hold the daily normals returned for the dates
    normals_greater_than_equal_to_start_date =[]

    # Use the start date and max date to create a range of dates
    # Save a list of %Y-%m-%d strings
    # Loop through the list of %Y-%m-%d strings and calculate the normals for each date
    # Push each tuple of calculations into a list called `normals_greater_than_equal_to_start_date`
    while (start_date_only_formatted <= max_date_formatted):
        specified_start_date.append(dt.datetime.strftime(start_date_only_formatted,'%Y-%m-%d'))
        datestr = dt.datetime.strftime(start_date_only_formatted,'%Y-%m-%d')
        normals_greater_than_equal_to_start_date.append(list(np.ravel(daily_normals(datestr))))
        start_date_only_formatted = start_date_only_formatted + dt.timedelta(days = 1)
    
    # Close the session
    session.close

    # Return a JSON list of the minimum, average and maximum temperatures for the dates in scope
    return jsonify(normals_greater_than_equal_to_start_date)



# ============================================================================================
# API - CALCULATE MIN, AVG, MAX TEMP FOR ALL DATES BETWEEN THE PROVIDED START AND END DATES
# Return a JSON list of the minimum temperature, the average temperature, and the max temperature 
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates 
# between the start and end date inclusive
# =============================================================================================

@app.route("/api/v1.0/temp_date_range/<start>/<end>")
def calc_stats(start=None, end=None):
    """Return a json list of the minimum temperature, the average temperature, and the max temperature. 
    When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive"""

    # Start a session to query the database
    session = Session(engine)
        
    # Format the specified start date
    import datetime as dt
    start_date = start
    start_date_formatted = dt.datetime.strptime(start_date, '%Y-%m-%d')

    # Format the specified end date
    end_date = end
    end_date_formatted = dt.datetime.strptime(end_date, '%Y-%m-%d')

    # Create a function that calculates the "daily normals" 
    # This function calculates the minimum, average and maximum temperature for a specified date
    def daily_normals(date):
        """Daily Normals.
        Args:
        date (str): A date string in the format '%Y-%m-%d'
        Returns:
        A list of tuples containing the daily normals, tmin, tavg, and tmax
        """
    
        sel = [Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
        return session.query(*sel).filter(func.strftime('%Y-%m-%d', Measurement.date) == date).all()

    # Create a list to contain the dates
    specified_start_and_end_dates = []

    # Create a list to hold the daily normals returned for the dates
    normals_bw_start_and_end_dates =[]

    # Use the start date and end date to create a range of dates
    # Save a list of %Y-%m-%d strings
    # Loop through the list of %Y-%m-%d strings and calculate the normals for each date
    # Push each tuple of calculations into a list called `normals_bw_start_and_end_dates`    
    while (start_date_formatted <= end_date_formatted):
        specified_start_and_end_dates.append(dt.datetime.strftime(start_date_formatted,'%Y-%m-%d'))
        datestr = dt.datetime.strftime(start_date_formatted,'%Y-%m-%d')
        normals_bw_start_and_end_dates.append(list(np.ravel(daily_normals(datestr))))
        start_date_formatted = start_date_formatted + dt.timedelta(days = 1)

    # Close the session
    session.close

    # Return a JSON list of the minimum, average and maximum temperatures for the dates in scope
    return jsonify(normals_bw_start_and_end_dates)



if __name__ == '__main__':
    app.run(debug=True)




