from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

MENU = {
    "Капучино": 80,
    "Лате": 85,
    "Еспресо": 60,
    "Чізкейк": 120,
    "Панкейки": 95,
}


@app.route("/")
def index():
    current_time = datetime.now()
    current_hour = current_time.hour
    return render_template(
        "index.html", cafe_name="Космічна Кава", current_hour=current_hour
    )


@app.route("/menu")
def menu_page():
    current_day = datetime.now().strftime("%A")
    return render_template(
        "menu.html", title="Наше Меню", menu=MENU, current_day=current_day
    )


if __name__ == "__main__":
    app.run(debug=True)
