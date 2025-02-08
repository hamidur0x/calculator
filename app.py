from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cal", methods=["POST"])
def calculation():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        work = request.form["work"]

        if work == "+":
            ans = num1 + num2
        elif work == "-":
            ans = num1 - num2
        else:
            ans = "404"  # Error for unsupported operation

        return render_template("index.html", result=ans)

    except ValueError:
        return render_template("index.html", result="Invalid input. Please enter valid numbers.")

if __name__ == '__main__':
    app.run(debug=True)
