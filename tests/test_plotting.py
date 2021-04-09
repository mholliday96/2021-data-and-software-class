"""This file contains all tests for our plotting library."""

import sys
import os
import pandas as pd
import src.clinker_plotter as plotting

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

def test_read_data():
    """A test for the read_data() function."""
    input_file = "clinker_data_p3.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    clinker_data = plotting.read_data(input_filename, starting_row=0)

    assert clinker_data.shape == (12,10)
    assert(clinker_data[1,1] == 84.6)

def test_convert_data():
    """A test for the convert_data() function."""
    input_file = "clinker_data_p3.csv"
    json_output_file = "data_output.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename = os.path.join(data_directory,input_file)
    json_filename = os.path.join(results_directory,json_output_file)

    plotting.convert_data(input_filename, json_filename)

    input_data = pd.read_csv(input_filename, index_col='SiO2', header=0)
    output_data = pd.read_json(json_filename)

    assert input_data.info() is output_data.info()

def test_plot():
    """A test for the plot() function."""
    assert plotting.plot() is None