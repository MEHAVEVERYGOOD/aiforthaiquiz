from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    print("[API1] รับคำขอจาก User")
    response = requests.get('http://api2:1234/')
    print("[API1] ได้คำตอบจาก API2:", response.text)
    return jsonify({
        "api1": "ginaraidee from api1",
        "api2_response": response.text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
