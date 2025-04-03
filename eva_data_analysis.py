import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by date

    Args:
        input_file_ (str): The path to the JSON file.

    Returns:
         eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe structure
    """
    # read in json file
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    # convert eva column to float
    eva_df['eva'] = eva_df['eva'].astype(float)
    # removing missing values
    eva_df.dropna(axis=0, inplace=True)
    # sort values by date
    eva_df.sort_values('date', inplace=True)
    return eva_df

def write_dataframe_to_csv(df, output_file):
    """
    Write the dataframe to a CSV file.

    Args:
        df (pd.DataFrame): The input dataframe.
        output_file (str): The path to the output CSV file.

    Returns:
        None
    """
    
    # write out data to csv
    df.to_csv(output_file, index=False)

# Main code

# Data source is https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r',encoding='utf-8')
output_file = open('./eva-data.csv','w',encoding='utf-8')
graph_file = './cumulative_eva_graph.png'

print("---START---")

# Read the data from JSON file
eva_data = read_json_to_dataframe(input_file)

# Convert and export data to CSV file
write_dataframe_to_csv(eva_data, output_file)


# create new column duration hours
eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()

# Plot cumulative spacewalk duration and save to file
print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
print("--END--")