import sqlite3
from flask import Flask, request, jsonify
def create_app():
    app = Flask(__name__)
    def init_db():
        with sqlite3.connect('messages.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                 ''')
            conn.commit()
    def add_message_to_db(content):

        with sqlite3.connect('messages.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO messages (content) VALUES (?)', (content,))
            conn.commit()
    @app.route('/messages', methods=['POST'])
    def save_message():

        if not request.is_json:
            return jsonify({"error": "Expected JSON data"}), 400
        data = request.get_json()
        content = data.get('content')
        if not content:
            return jsonify({"error": "Missing 'content' in the request body"}), 400
        add_message_to_db(content)
        return jsonify({"message": "Message saved successfully"}), 200
    init_db()
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(port=8000)