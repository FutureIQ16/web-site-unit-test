from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        c = float(request.form['c'])

        discriminant = b ** 2 - 4 * a * c

        if discriminant < 0:
            roots = "Корней нет"
        elif discriminant == 0:
            root = -b / (2 * a)
            roots = f"Один корень: {root}"
        else:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            roots = f"Корень 1: {root1}, Корень 2: {root2}"

        return render_template('index.html', roots=roots)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
