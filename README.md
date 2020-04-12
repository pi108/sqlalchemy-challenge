# sqlalchemy-challenge

# An Analysis of Temperature and Precipitation Data for 9 Stations in Honolulu, Hawaii using SQL-Alchemy, Pandas, Scipy, Matplotlib and Flask:

## This repository contains the following:
A folder called Resources
A folder called Output
A jupyter notebook file called “climate_analysis”
A python file called “climate_app”

### Folder called Resources:
This folder contains 2 csv files as follows:<br>
1. hawaii_stations.csv<br>
2. hawaii_measurements.csv<br>
This folder also contains the following SQLite database file:<br>
3. hawaii.sqlite
This SQLite database contains 2 tables:<br>
3-A. Station: This table contains the data in the csv file called “hawaii_stations” mentioned above.<br>
3-B. Measurement:  This table contains the data in the csv file called “hawaii_measurements” mentioned above. 

### Folder called Output:
This Folder contains the charts that were generated as part of the analysis using the jupyter notebook file. There are 4 charts as follows:
1.	A LINE Chart that shows the precipitation levels across all 9 stations, for the last 12 months in the dataset (08/23/2016 to 08/23/2017).
2.	A HISTOGRAM Chart that shows the temperatures observed for the most active station, “USC00519281”, which corresponds to “WAIHEE 837.5, HI, US”), for  the last 12 months in the dataset (08/23/2016 to 08/23/2017).
3.	A BAR Chart that shows the average temperature for the period one year prior (12/01/2016 to 12/09/2016) for fictitious proposed trip dates of 12/01/2017 to 12/09/2017. This chart also shows an error bar which is calculated as the difference between the Maximum and the Minimum Temperature for the same period (12/01/2016 to 12/09/2016).
4.	A STACKED Chart that shows the minimum, average and maximum temperatures for the Month-Date combination for all available prior years from this dataset. So, in this case, we analyzed the temperatures for the dates: 12/01 to 12/09 for the years 2010 to 2016.

### Jupyter Notebook File called “climate_analysis”:
This file contains the detailed analysis that was done on the provided dataset using SQL-Alchemy, Pandas, Scipy and MatplotLib. Analysis was done regarding:
1)	The Precipitation Levels for the last 12 months in the dataset (the period 2016-08-23 to 2017-08-23).
2)	The list of all the weather stations in Hawaii.
3)	The most active station in the dataset.
4)	The Temperature Observations for the most active station for the last 12 months in the dataset (the period 2016-08-23 to 2017-08-23).
5)	The mean temperatures for June and December for the entire period of the dataset (01/01/2010 to 08/23/2017).
6)	An unpaired independent t-test between the means of the June and December temperatures for the entire period of the dataset (01/01/2010 to 08/23/2017). 
7)	The minimum, average and maximum temperatures for a set of fictitious proposed trip dates. We calculated these based on the temperatures for the same dates for the period one year prior, from this dataset. We assumed proposed trip dates of 12/01/2017 to 12/09/2017. We looked up the temperatures for the period one year prior, from this dataset (12/01/16 to 12/09/16). 

### Python file called “climate_app”:
This file contains an app that was built using SQL-Alchemy and Flask.
This app contains a home page and the following routes that are accessible via the home page:
1)	The Precipitation Levels from 2016-08-23 to 2017-08-23:
•	/api/v1.0/precipitation 
2)	The list of all the weather stations in the dataset:
•	/api/v1.0/stations
3)	The Temperature Observations for the most active station “USC00519281”, which corresponds to “WAIHEE 837.5, HI, US”, from 2016-08-23 to 2017-08-23:
•	/api/v1.0/tobs
4)	The Minimum, Average and Maximum Temperature from the user-specified start date till the end date in the dataset, which is 08/23/2017. The user will need to enter the start date in the format 2016-12-01.
•	/api/v1.0/temp_from_start_date/
5)	The Minimum, Average and Maximum Temperatures from the user-specified start date till the user-specified end date. The user will need to enter the start date and end dates in the format 2016-12-01.
•	/api/v1.0/temp_date_range//

# Conclusions:
Based on our analysis, we conclude the following:

## Total Number of Stations:
There were 9 Stations in the dataset as follows:<br>
	Station,	    Station Name,	                      	Latitude,	Longitude,	  Elevation <br>
1	USC00519397,	WAIKIKI  717.2, HI US,	                  	21.27, 	  	(157.82),	  3.00 <br>
2	USC00513117,	KANEOHE 838.1, HI US,	                  	21.42,	  	(157.80),	  14.60 <br>
3	USC00514830,	KUALOA RANCH HEADQUARTERS 886.9, HI US,		21.52, 	  	(157.84),	  7.00 <br>
4	USC00517948,	PEARL CITY, HI US,	                      	21.39, 	  	(157.98),	  11.90 <br>
5	USC00518838,	UPPER WAHIAWA 874.3, HI US,	            	21.50, 	  	(158.01),	  306.60 <br>
6	USC00519523,	WAIMANALO EXPERIMENTAL FARM, HI US,	    	21.34, 	  	(157.71),	  19.50 <br>
7	USC00519281,	WAIHEE 837.5, HI US,	                    	21.45, 	  	(157.85),	  32.90 <br>
8	USC00511918,	HONOLULU OBSERVATORY 702.2, HI US,	      	21.32, 	  	(158.00),	  0.90 <br>
9	USC00516128,	MANOA LYON ARBO 785.2, HI US,	          	21.33, 	  	(157.80),	  152.40 <br>

## The Precipitation Levels for the last 12 months of the dataset (08/23/2016 to 08/23/2017):
We had a total of 2021 precipitation observations during this period. <br>
The minimum precipitation was 0 inches. <br>
The average precipitation was 0.177 inches. <br>
The maximum precipitation was 6.7 inches. <br>
The standard deviation of the precipitation was 0.46 inches. <br>

## The Most Active Station in the dataset:
The station with the greatest number of observations was: <br>
Station “USC00519281”, which corresponds to “WAIHEE 837.5, HI, US”. <br> 
This station had 2772 rows in the dataset. <br>

## The Temperature Observations, for the Most Active Station (“USC00519281”), for the entire period of the dataset (01/01/2010 to 08/23/2017):
The minimum temperature observed for this station was 54.00 degrees Fahrenheit. <br>
The average temperature observed for this station was 71.66 degrees Fahrenheit. <br>
The maximum temperature observed for this station was 85.00 degrees Fahrenheit. <br>

## The Temperature Observations, for the Most Active Station (“USC00519281”), for the last 12 months of the dataset (08/23/2016 to 08/23/2017):
The minimum temperature observed for this station was 59.00 degrees Fahrenheit. <br>
The average temperature observed for this station was 73.11 degrees Fahrenheit. <br>
The maximum temperature observed for this station was 83.00 degrees Fahrenheit. <br>
The Histogram "bin" or bucket with the highest number of observations was Temperature 75 to 77. <br>

## Relationship between the mean temperatures in June and December over the entire period of the dataset (01/01/2010 to 08/23/2017): 
The mean temperature for June was 74.94 degrees Fahrenheit. <br>
The mean temperature for December was 71.04 degrees Fahrenheit.  <br>
The difference between the mean temperatures for June and December was 3.90 degrees Fahrenheit.  <br>
The key question which then arises is: Is this difference statistically significant, OR Could this difference have been purely based on chance. <br>
So, we ran an unpaired independent t-test between the temperatures observed in June and December for the entire dataset (01/01/2010 to 08/23/2017).  <br>
The p-value returned from this test was significantly lower than 0.05 implying that there is a less than 5% probability that the differences in the means between the June and December temperatures is only because of chance. <br>
In other words, we can conclude that there is a statistically significant difference in the means between the June and the December temperatures in this dataset. <br>

## Analysis of temperatures for fictitious proposed trip dates using prior year data: 
We picked a set of fictitious trip dates: 12/01/2017 to 12/09/2017. <br>
We then analyzed the temperatures for the same Month-Date combination but for the prior year, from this dataset. <br>
So, in this case, we analyzed the temperatures for the dates: 12/01/16 to 12/09/16. <br>
The minimum temperature was 67.00 degrees Fahrenheit. <br>
The average temperature was 71.32 degrees Fahrenheit. <br>
The maximum temperature was 77.00 degrees Fahrenheit. <br>

## Analysis of total precipitation levels for fictitious trip dates: 
We picked a set of fictitious trip dates: 12/01/2017 to 12/09/2017. <br>
We then analyzed the total precipitation levels for the same Month-Date combination but for the prior year, from this dataset. <br> 
So, in this case, we analyzed the total precipitation levels for the dates: 12/01/16 to 12/09/16. <br>
The results were as follows: <br>
Station,  	    Total Precipitation (inches) <br>
USC00516128, 	  5.99 <br>
USC00519281, 	  2.25 <br>
USC00513117, 	  1.67 <br>
USC00514830, 	  1.21 <br>
USC00519397, 	  1.18 <br>
USC00519523, 	  1.04 <br>
USC00517948,	  0.27 <br>

## Analysis of temperatures for fictitious trip dates using the same Month-Date combination from all available years in the dataset: 
We picked a set of fictitious trip dates: 12/01/2017 to 12/09/2017. <br>
We then analyzed the temperatures for the same Month-Date combination for all available prior years, from this dataset. <br>
So, in this case, we analyzed the minimum, average and maximum temperatures for the dates 12/01 to 12/09 for the years 2010 to 2016. <br>
The results were as follows: <br>
Date,	  Min,	  	    Avg,	    Max <br>
12/1,	  65.00, 	    71.92, 	    78.00  <br>
12/2,	  62.00, 	    71.33, 	    77.00  <br>
12/3,	  67.00, 	    72.89, 	    79.00  <br>
12/4,	  66.00, 	    72.18, 	    81.00  <br>
12/5,	  64.00, 	    70.92, 	    78.00  <br>
12/6,	  61.00, 	    69.39, 	    78.00  <br>
12/7,	  58.00, 	    69.20, 	    79.00  <br>
12/8,	  60.00, 	    70.27, 	    83.00  <br>
12/9,	  64.00, 	    71.90, 	    80.00 <br>


