from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

menu = {
    "Burger": 50,
    "Pizza": 80,
    "Cola": 20
}

orders = []

@app.route("/", methods=["GET", "POST"])
def home():
    total = 0

    if request.method == "POST":
        item = request.form["item"]
        qty = int(request.form["qty"])
        price = menu[item] * qty
        orders.append((item, qty, price))

    for o in orders:
        total += o[2]

    tax = total * 0.14
    final = total + tax

    return render_template("index.html", menu=menu, orders=orders, total=total, tax=tax, final=final)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
