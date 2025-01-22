from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta
def create_app():
    app = Flask(__name__)
    def fetch_exchange_rate(target_date, currency_code="USD"):
        url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange"
        params = {
            "json": "",
            "date": target_date.strftime('%Y%m%d'),
            "valcode": currency_code
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data[0]["rate"] if data else None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return None
    @app.route("/currency", methods=["GET"])
    def currency():
        param = request.args.get("param", "").lower()
        today = datetime.today()
        if param == "today":
            target_date = today
        elif param == "yesterday":
            target_date = today - timedelta(days=1)
        else:
            return jsonify({"error": "Please use 'today' or 'yesterday' as the 'param' query parameter."}), 400
        rate = fetch_exchange_rate(target_date)
        if rate is not None:
            return jsonify({
                "date": target_date.strftime('%Y-%m-%d'),
                "currency": "USD",
                "rate": rate
            })
        else:
            return jsonify({"error": f"Unable to fetch the exchange rate for {target_date.strftime('%Y-%m-%d')}"}), 500
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(port=8000)