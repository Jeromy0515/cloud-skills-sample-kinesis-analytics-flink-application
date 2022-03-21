import datetime
import json
import random

def get_data():
    return {
        'EVENT_TIME': datetime.datetime.now().isoformat(),
        'TICKER': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'PRICE': round(random.random() * 100, 2)}


def generate():
    f = open('app.log','w')
    while True:
        data = json.dumps(data)
        f.write(data)

if __name__ == '__main__':
    generate()