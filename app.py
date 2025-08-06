from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    height = None
    weight = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            bmi = round(weight / ((height / 100) ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
        except:
            bmi = None
            category = "Invalid input"

    return render_template('index.html', bmi=bmi, category=category, height=height, weight=weight)

if __name__ == '__main__':
    app.run(debug=True)

