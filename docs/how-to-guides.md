# How to change the destination file path of Spacewalk's output

This how-to guide shows you how to change the destination path for the dataset created when running Spacewalk's data analysis to a location of your choice.

The spacewalk data analysis script generates a data set in CSV format (file name eva-data.csv), which by default is saved to the `results/` folder in the working directory.

If you would like to modify the name or location of the output dataset, set the
second command line argument to your chosen file path.
For example, if you want to save the output data set to the subfolder `data/clean/` you can
invoke the script as:

python eva_data_analysis.py eva-data.json data/clean/eva-data-clean.csv

The specified destination folder `data/clean/` must exist before running spacewalks analysis script.