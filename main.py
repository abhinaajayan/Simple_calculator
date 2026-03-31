from flask import Flask, render_template, request
import math  # ✅ Import math module

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = request.form.get("num2")  # optional for some operations
            operation = request.form["operation"]

            # Convert num2 only if needed
            if num2:
                num2 = float(num2)

            # 🔢 Basic operations
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

            # 🔬 Scientific operations
            elif operation == "sin":
                result = math.sin(math.radians(num1))  # degrees → radians
            elif operation == "cos":
                result = math.cos(math.radians(num1))
            elif operation == "tan":
                result = math.tan(math.radians(num1))
            elif operation == "log":
                result = math.log10(num1)
            elif operation == "sqrt":
                result = math.sqrt(num1)
            elif operation == "power":
                result = num1 ** num2

        except Exception as e:
            result = "Invalid Input"

    return render_template("index.html", result=result)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)