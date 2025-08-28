    mapcenter = [data['LAT'].mean(), data['LON'].mean()]
    mapheat = folium.Map(location=mapcenter, zoomstart=11)
    style_html = """
    <style>
      body { margin:0; padding:0; }
      html, body, #map {
        width: 100%;
        height: 100%;
      }
    </style>
    """
    map_heat.get_root().html.add_child(folium.Element(style_html))
    heat_data = [[row['LAT'], row['LON']] for _, row in data.iterrows()]
    HeatMap(heat_data).add_to(map_heat)
    mapheat_file = os.path.join(output_dir_path, 'heatmap_crimes.html')
    map_heat.save(mapheat_file)
    print(f"Saved heatmap of all crimes to: {mapheat_file}")