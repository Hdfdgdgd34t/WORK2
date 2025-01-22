from flask import Flask, request, jsonify, make_response
import dicttoxml
def create_app():
    app = Flask(__name__)
    @app.route("/currency", methods=["GET"])
    def fetch_currency():
        exchange_rate = {"currency": "USD", "rate": 42}
        content_type = request.headers.get("Content-Type", "text/plain")
        if content_type == "application/json":
            return jsonify(exchange_rate)
        elif content_type == "application/xml":
            xml_data = dicttoxml.dicttoxml(exchange_rate, custom_root="exchange_rate", attr_type=False)
            response = make_response(xml_data)
            response.headers["Content-Type"] = "application/xml"
            return response
        else:
            return "Unsupported Content-Type. Please use 'application/json' or 'application/xml'.", 415
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(port=8000)