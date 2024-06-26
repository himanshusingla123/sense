import requests

def monitor_model():
    response = requests.get('http://model-monitoring-service/metrics')
    metrics = response.json()
    return metrics

def main():
    metrics = monitor_model()
    print(metrics)

if __name__ == '__main__':
    main()
