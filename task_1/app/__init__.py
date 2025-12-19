from flask import Flask

# 1. Сначала создаем переменную app
app = Flask(__name__)

# 2. И только ПОТОМ импортируем маршруты
from app import routes