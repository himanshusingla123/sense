import pandas as pd
from sklearn.impute import SimpleImputer

def clean_data(data):
    # Handling missing values
    imputer = SimpleImputer(strategy='mean')
    data.iloc[:, 1:] = imputer.fit_transform(data.iloc[:, 1:])
    return data

def preprocess_data(data):
    # Additional preprocessing steps
    data['sensor_1'] = data['sensor_1'].rolling(window=3).mean()
    data['sensor_2'] = data['sensor_2'].rolling(window=3).mean()
    data['sensor_3'] = data['sensor_3'].rolling(window=3).mean()
    return data.dropna()

def main():
    data = pd.read_csv('raw_data.csv')
    data = clean_data(data)
    data = preprocess_data(data)
    data.to_csv('preprocessed_data.csv', index=False)

if __name__ == '__main__':
    main()
