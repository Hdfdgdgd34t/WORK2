from flask import Flask, request, jsonify
def create_app():
    app = Flask(__name__)

    @app.route("/currency", methods=["GET"])
    def fetch_currency():
        today = request.args.get("today", "not provided")
        key = request.args.get("key", "not provided")
        exchange_rate = {"currency": "USD", "rate": 42}
        response = {
            "message": "Exchange rate retrieved successfully",
            "exchange_rate": exchange_rate,
            "parameters": {"today": today, "key": key}
        }
        return jsonify(response)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(port=8000)