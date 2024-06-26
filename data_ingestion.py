import pandas as pd
import numpy as np

def fetch_sensor_data():
    # Simulating sensor data fetching
    data = {
        'timestamp': pd.date_range(start='1/1/2020', periods=1000, freq='H'),
        'sensor_1': np.random.randn(1000),
        'sensor_2': np.random.randn(1000),
        'sensor_3': np.random.randn(1000),
    }
    return pd.DataFrame(data)

def fetch_database_data():
    # Simulating database data fetching
    data = {
        'timestamp': pd.date_range(start='1/1/2020', periods=1000, freq='H'),
        'maintenance_needed': np.random.randint(0, 2, size=(1000,))
    }
    return pd.DataFrame(data)

def main():
    sensor_data = fetch_sensor_data()
    database_data = fetch_database_data()
    data = pd.merge(sensor_data, database_data, on='timestamp')
    data.to_csv('raw_data.csv', index=False)

if __name__ == '__main__':
    main()
