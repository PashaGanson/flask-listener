
from flask import Flask, request, jsonify
import requests

# Создаем приложение Flask
app = Flask(__name__)

# URL вашего Google Apps Script
WEB_APP_URL = 'https://script.google.com/macros/s/AKfycbx5RDv2E0CMYQ6nx7gMeS9D0rMsr1sJ_KRnsV2wS_nh8CVwzdCXg5EfjGEb6c_2T0Gv-w/exec'

# Маршрут для обработки POST-запросов
@app.route('/add_food', methods=['POST'])
def add_food():
    # Получаем данные из запроса
    user_data = request.json

    # Отправляем данные в Google Apps Script
    response = requests.post(WEB_APP_URL, json=user_data)

    # Возвращаем ответ от Google Apps Script
    return jsonify({"status": "success", "response": response.text})

# Локальный запуск приложения (для отладки)
if __name__ == '__main__':
    app.run()