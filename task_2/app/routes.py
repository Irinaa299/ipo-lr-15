from flask import jsonify, request
from datetime import datetime
from app import app # Теперь это сработает

@app.route('/sum')
def sum_numbers():
    # ваш код ...
    return "Сумма"

@app.route('/info')
def info():
    # ваш код ...
    return jsonify({"status": "ok"})
