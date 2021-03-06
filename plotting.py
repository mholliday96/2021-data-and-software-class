#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
#import tasplot
import pandas as pd

# Create an array (a multi-dimensional table) out of our data file, full of text
all_clinker_data = np.genfromtxt("clinker_data_p3.csv", delimiter=',',skip_header=1)


# Select the data range we are interested in, convert it into a new array, full of numbers
clinker_data = np.array(all_clinker_data[1:,2:], dtype=float)
print(clinker_data)

# Compute a total alkali column by summing two columns together
total_alkali = ((clinker_data[:,7]) + (clinker_data[:,8]))
print(total_alkali)

# Append this new column to the existing temperature_data array
processed_clinker_data = np.append(clinker_data, total_alkali,1)
print (processed_clinker_data)

# Create a figure of the processed data
clinker_figure = plt.figure()
clinker_plot = plt.plot(processed_clinker_data[:,0],processed_clinker_data[:,9])
plt.show(block=True)

#Create the TAS format as per 2015 John A Stevenson @volcan01010
silica = [50, 60, 70, 80]
total_alkalis = [2, 3, 4, 5, 6]

ax1 = fig.subplot(111)
#tasplot.add_LeMaitre_fields(ax1)
plt.plot(silica, total_alkalis)

#show figure
total_alkali_figure.savefig('./TAS_clinkers.png')



#all_data = pd.read_csv("110-tavg-12-12-1950-2020.csv", index_col='Date', header=4)
#all_data.info()
#all_data.to_json("data_output.json")

#json_data = pd.read_json("data_output.json")
#json_data.info()

#print(json_data.loc['195012':'197512','Value'])