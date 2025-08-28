import pandas as pd
import folium
import os
from folium.plugins import HeatMap
def create_crime_map():
    data= 'Crime_data_2020_to_present.csv'
    output_folder = 'Crime_Maps'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir, data)
    output_dir_path = os.path.join(current_dir, output_folder)
    os.makedirs(output_dir_path, exist_ok=True)
    try:
        data = pd.read_csv(csv_file_path, nrows=10000)
        print("Successfully loaded the first 10,000 rows of the CSV file.")
    except FileNotFoundError:
        print(f"Error '{data}'. "
              "Please ensure the file is in the same directory as the script.")
        return
    required_cols = ['DATE OCC', 'LAT', 'LON', 'Crm Cd Desc']
    if not all(col in data.columns for col in required_cols):
        print(f"Error: : {required_cols}")
        return

   