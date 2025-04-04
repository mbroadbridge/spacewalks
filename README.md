# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12
installed. You will also need the following libraries:

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation 

## Installation instructions

- clone repository from GitHub using Git:
git clone https://github.com/mbroadbridge/spacewalks.git

- install dependencies using pip (package details are in requirements.txt)
python -m pip install  matplotlib==3.8.4 numpy==2.0.0 pytest==7.4.2 pandas==2.2.2

- test code using pytest:
python -m pytest

## Usage Example

- Launch the eva_data_analysis.py script from the command line using python:
python eva_data_analysis.py data/eva-data.json results/eva-data.csv