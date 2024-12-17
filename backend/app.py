from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Time Service API",
        "current_time": datetime.now().isoformat(),
        "server_timezone": str(datetime.now().astimezone().tzinfo)
    })

@app.route('/time')
def get_time():
    return jsonify({
        "current_time": datetime.now().isoformat(),
        "utc_time": datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
