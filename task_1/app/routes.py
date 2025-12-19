from app import app

@app.route('/')  # Если этого нет, главная даст 404
def index():
    return "Приветствие"

@app.route('/hello/<name>') # Проверьте слеши и скобки <>
def hello(name):
    return f"Привет, {name}!"

@app.route('/square/<int:number>')
def square(number):
    return f"Квадрат: {number**2}"
