import pandas as pd

def engineer_features(data):
    # Creating new features
    data['sensor_1_diff'] = data['sensor_1'].diff()
    data['sensor_2_diff'] = data['sensor_2'].diff()
    data['sensor_3_diff'] = data['sensor_3'].diff()
    data['sensor_1_squared'] = data['sensor_1'] ** 2
    data['sensor_2_squared'] = data['sensor_2'] ** 2
    data['sensor_3_squared'] = data['sensor_3'] ** 2
    return data.dropna()

def main():
    data = pd.read_csv('preprocessed_data.csv')
    data = engineer_features(data)
    data.to_csv('features.csv', index=False)

if __name__ == '__main__':
    main()
