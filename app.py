from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def exchange_rate():
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        response.raise_for_status()  # ensure the request was successful
        data = response.json()
        inr_rate = data['rates'].get('INR', 'Not Available')
        return f"<h1>1 USD = {inr_rate} INR</h1>"
    except Exception as e:
        return f"<h2>Error fetching exchange rate: {str(e)}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
