        data['DATE OCC'] = pd.to_datetime(data['DATE OCC'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    data = data.dropna(subset=['DATE OCC', 'LAT', 'LON'])
    data = data[data['DATE OCC'].dt.year >= 2020]
    if data.empty:
        print("Warning: No data available after filtering by year >= 2020.")
        return
    print(f"Total number of records processed: {len(data)}")