import csv
import numpy as np
import pandas

colnames = ['year', 'month', 'day', 'hour', 'postcode', 'rating'] 
data = pandas.read_csv('uksnow-July_to_Dec2015.csv', names=colnames)
postcode = data.postcode.tolist()
print (postcode)
year = data.year.as_matrix()
print (year)
month = data.month.as_matrix()
print (month)
day = data.day.as_matrix()
print (day)
hour = data.hour.as_matrix()
print (hour)
rating = data.rating.as_matrix()
print (rating)

