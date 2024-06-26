import pandas as pd
import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    return report

def main():
    data = pd.read_csv('features.csv')
    X = data.drop(['timestamp', 'maintenance_needed'], axis=1)
    y = data['maintenance_needed']
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    report = evaluate_model(model, X_test, y_test)
    print(report)

if __name__ == '__main__':
    main()
