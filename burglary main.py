    crimetype = 'BURGLARY'
    maptype = folium.Map(location=map_center, zoomstart=11)
    maptype.get_root().html.add_child(folium.Element(style_html))

    subset = data[data['Crm Cd Desc'].str.upper() == crime_type.upper()]
    print(f"Number of records found for '{crime_type}': {len(subset)}")

    if subset.empty:
        print(f"Warning: No data found for crime type '{crime_type}'. "
              "Check your CSV file for this crime description. No map was generated.")
    else:
        print(f"Found {len(subset)} records for '{crime_type}'. Generating map...")
        for _, row in subset.iterrows():
            folium.Marker(
                location=[row['LAT'], row['LON']],
                popup=f"{row['Crm Cd Desc']} ({row['DATE OCC'].date()})",
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(map_type)
        maptype_file = os.path.join(output_dir_path, f'{crimetype.lower()}_map.html')
        map_type.save(map_typefile)
        print(f"Saved {crimetype} map to: {map_typefile}")
if __name__ == '__main__':
    create_crimemap()
