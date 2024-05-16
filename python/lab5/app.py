from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
from dingtalkchatbot.chatbot import DingtalkChatbot
import requests
import json
from datetime import datetime

app = Flask(__name__)

# 数据库配置
db_config = {
    'user': 'root',
    'password': 'zzy123456',
    'host': 'localhost',
    'database': 'SensorData',
    'raise_on_warnings': True
}

def get_data(type):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT value FROM " + type + " ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'  # 允许所有来源访问，也可以设置为具体的来源
    return response

@app.route('/data')
def data():
    temperature = get_data("temperature")
    humidity = get_data("humidity")
    pressure = get_data("pressure")

    result = {
        "temperature": temperature[0][0],
        "humidity": humidity[0][0],
        "pressure": pressure[0][0]
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
