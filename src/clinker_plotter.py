#!/bin/python

"""This is a simple plotting script written for future reference"""

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(filename, delimiter =','):
    """this function reads data from a specific filename.
    specified file should read to .csv"""

    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_clinker_data = np.genfromtxt(filename, delimiter=delimiter)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    data_array = np.array(all_clinker_data[1:,2:], dtype=float)
    return data_array

 #lt_data = read_data(input_file)

def process_data(data_array):
    """this function adds Na2O and K2O columns for total alkali count"""

# Compute a total alkali column by summing two columns together
    total_alkali = ((data_array[:,7]) + (data_array[:,8]))

# Append this new column to the existing temperature_data array
    processed_clinker_data = np.append(data_array, total_alkali, 1)
    return processed_clinker_data

def convert_data(filename, output_filename):
    """This converts data to .json"""
    all_data = pd.read_csv(filename, index_col='SiO2', header=0)
    all_data.info()
    all_data.to_json(output_filename)

def plot_data(processed_clinker_data, plot_filename):
    """This takes processed data and generates a figure"""
    # Create a figure of the processed data
    tas_figure = plt.figure()
    plt.plot (processed_clinker_data[:,1],processed_clinker_data[:,2])

    plt.show(block=True)
    tas_figure.savefig(plot_filename)

# Create a figure of the processed data
def plot():
    """Final figure plotting"""
    input_file = "clinker_data_p3.csv"
    plot_file = "TAS_clinkers.png"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename = os.path.join(data_directory,input_file)
    plot_filename = os.path.join(results_directory,plot_file)
    json_filename = os.path.join(results_directory,json_output_file)

    clinker_data = read_data(input_filename)
    processed_clinker_data = process_data(clinker_data)
    plot_data(processed_clinker_data, plot_filename)
    convert_data(input_filename, json_filename)

#show figure
#total_alkali_figure.savefig('./TAS_clinkers.png')


if __name__ == "__main__":
    print(sys.argv)
    plot()
