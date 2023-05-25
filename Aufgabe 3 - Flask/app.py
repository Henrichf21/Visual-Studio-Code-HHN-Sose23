from flask import Flask, render_template
from repo.db import get_all_customer,insert_customer
app = Flask(__name__)

@app.route('/')
def index():
    customer=get_all_customer()
    return render_template("index.html",customer=customer)

if __name__ == '__main__':
    app.run(debug=True)