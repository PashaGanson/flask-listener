from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbx5RDv2E0CMYQ6nx7gMeS9D0rMsr1sJ_KRnsV2wS_nh8CVwzdCXg5EfjGEb6c_2T0Gv-w/exec'

@app.route('/add_food', methods=['POST'])
def add_food():
    user_data = request.json
    response = requests.post(WEB_APP_URL, json=user_data)
    return jsonify({"status": "success", "response": response.text})

if __name__ == '__main__':
    app.run()