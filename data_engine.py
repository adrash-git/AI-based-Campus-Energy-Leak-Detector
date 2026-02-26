import pandas as pd
import numpy as np

def generate_mock_data():
    rooms = ['Seminar Hall', 'Lab 101', 'Library', 'Cafeteria', 'Staff Room']
    data = []
    for room in rooms:
        for hour in range(24):
            occupancy = 1 if 9 <= hour <= 17 else 0
            usage = np.random.uniform(0.1, 0.4) 
            if occupancy == 1:
                usage += np.random.uniform(1.5, 3.0)
            elif hour > 20 and np.random.random() > 0.7: 
                usage += 1.2 
            data.append([room, hour, occupancy, round(usage, 2)])
    return pd.DataFrame(data, columns=['Room', 'Hour', 'Occupancy', 'Usage_kW'])

def calculate_leak_scores(df):
    # Logic: High usage (Usage_kW) but low occupancy = High Leak Score
    df['Leak_Score'] = df.apply(
        lambda x: (x['Usage_kW'] * 20) if x['Occupancy'] == 0 and x['Usage_kW'] > 0.5 else 0, 
        axis=1
    )
    return df