import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def main():
    data = pd.read_csv('features.csv')
    X = data.drop(['timestamp', 'maintenance_needed'], axis=1)
    y = data['maintenance_needed']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = train_model(X_train, y_train)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    main()
