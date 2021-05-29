#!/usr/bin/env python
# coding: utf-8

# ## Problem 2 - Plotting temperatures 
# 
# In this problem we will  plot monthly mean temperatures from the Helsinki-Vantaa airpot for the past 30 years.
# 
# ## Input data
# 
# File `data/helsinki-vantaa.csv` monthly average temperatures from Helsinki Vantaa airport. Column descriptions:
# 
# ### Part 1
# 
# Load the Helsinki temperature data (`data/helsinki-vantaa.csv`)
# 
# - Read the data into variable called `data` using pandas
# - Parse dates from the column `'DATE'` and set the dates as index in the dataframe 

# YOUR CODE HERE 1 to read the data into data and parse dates
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
fp="data/helsinki-vantaa.csv"
# read the file. and analysis　'DATE' index change 'DATE'.
data=pd.read_csv(fp,parse_dates=['DATE'],index_col='DATE')
# This test print should print first five rows
print(data.head())

# Check the number of rows in the data frame
print(len(data))

# ### Part 2
# 
# Select data for a 30 year period (January 1988 - December 2018)
# 
# - Store the selection in a new variable `selection`

# YOUR CODE HERE 2
# create new colum because index is not int  
data["date"]=pd.to_datetime(data.index)
# select the data from 1988 to 2018
selection=data.loc[(data["date"].dt.year>=1988)&(data["date"].dt.year<=2018)]
# Check that the data was read in correctly:
selection.head()

# Check how many rows of data you selected:
print("Number of rows:", len(selection))


# ### Part 3
# 
# #### Part 3.1
# 
# Create a line plot that displays the temperatures (`TEMP_C`) for yeach month in the 30 year time period:
#      
# #### Part 3.2
# 
# Save your figure as PNG file called `temp_line_plot.png`.
# 

# YOUR CODE HERE 3
# create the table data
monthly_data=pd.DataFrame()
# Change datatype and use slice method to get the value that i want to get
selection['TIME_STR']=selection['date'].astype(str)
# Cut out each value
selection['YEAR']=selection['TIME_STR'].str.slice(start=0,stop=4)
# Cut out each value
selection['MONTH']=selection['TIME_STR'].str.slice(start=4,stop=6)
# Put together the data
grouped=selection.groupby(['YEAR','MONTH'])
# Put a value
mean_col=['TEMP_C']
# calculate the average for all group's TEMP_C
for key,group in grouped:
  # get the mean of TEMP_C
  mean_values=group[mean_col].mean()
  # Add mean_value to monthly_data
  monthly_data=monthly_data.append(mean_values,ignore_index=True)
selection_data=pd.DataFrame({'x':selection["date"],'y':selection["TEMP_C"]})

# setting of figure
selection_data.plot.line(x='x',y='y'
,style=['k.-'])

# change the tittle, xlabel and ylabel
plt.title("Helsinki-Vantaa Airport")
plt.xlabel("Time")
plt.ylabel("Temperature(Celsius)")
# Set output file name
outputfp = "temp_line_plot.png"

# Save plot as image
# YOUR CODE HERE 4
# save the data 
plt.savefig("temp_line_plot.png")
import os

#Check that output file exists (also open the file and check that the plot looks ok!)
os.path.exists(outputfp)


# **REMINDER**: Don't forget to upload your figure and the modified notebook into your personal GitHub repository!
# 
# ### Done!
