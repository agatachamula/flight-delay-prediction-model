# Flight delay prediction model

This project is a part of Bachelor Thesis for Computer Science Degree titled "System for predicting flight delays"

List of used packages:
* numpy
* pandas
* tkinter
* csv
* os
* functools
* sklearn
* coremltools

##Dataset

Dataset for training and testing is adapted from "Reporting Carrier On-Time Performance" [available here.] (https://www.transtats.bts.gov/tables.asp?DB_ID=120)
Data from 2002 to 2017 are used.

## Data cleaning and analysis

This process consists of:
* dealing with missing values
* droping and interchanging columns
* joing database files
* replacing strings with numerical values
* creating dictionaries to encode numerical values into strings
* sorting by airlines
* generating class of delay

After the cleaning some inital anaysis of delays is performed in regard to airlines, airports and time of departure. 
Measures for this analysis are count, max delay, min delay, sum of delays and mean delay expressed in minutes.
This is done with script get_basic_data.py

## Model training

Models were prepared using sklearn package. Training was done in Python 2.7.

Tested models were:
* Ridge Regression
* regression tree
* Support Vector Classification
* decision tree classifier

Decision tree classifier was used in the final project.

## Model export

Model was exported to format suitable for IOS application using coreMLtools.



