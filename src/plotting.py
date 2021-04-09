#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(filename = "clinker_data_p3.csv", delimiter =','):
    """this function reads data from a specific filename. 
    specified file should read to .csv"""
    
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_clinker_data = np.genfromtxt("clinker_data_p3.csv", delimiter=',',skip_header=1)
    
    # Select the data range we are interested in, convert it into a new array, full of numbers
    clinker_data = np.array(all_clinker_data[1:,2:], dtype=float)
    return clinker_data

clinker_data = read_data()

def process_data(filename = "clinker_data_p3.csv"):
# Compute a total alkali column by summing two columns together
    total_alkali = ((clinker_data[:,7]) + (clinker_data[:,8]))


# Append this new column to the existing temperature_data array
    processed_clinker_data = np.append(clinker_data, total_alkali,1)
    print (processed_clinker_data)

# Create a figure of the processed data
def plot():
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__), "..","data")) 
clinker_figure = plt.figure()
clinker_plot = plt.plot(processed_clinker_data[:,0],processed_clinker_data[:,9])
plt.show(block=True)

def convert_data(filename, output_filename):
    all_data = pd.read_csv(filename, index_col='silica', header=4)
    all_data.info()
    all_data.to_json(output_filename)

    input_filename = os.path.join(data_directory,input_file)
    plot_filename = os.path.join(results_directory,plot_file)
    json_filename = os.path.join(results_directory,json_output_file)

    clinker_data = read_data(input_filename, starting_row=0)
    processed_clinker_data = process_data(clinker_data)
    plot_data(processed_clinker_data, plot_filename)
    convert_data(input_filename, json_filename)

#show figure
total_alkali_figure.savefig('./TAS_clinkers.png')


if __name__ == "__main__":
    print(sys.argv)[1]
    plot()
