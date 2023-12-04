
# try to get yearly data, calcualte slope for each month and make predictions


from flask import Flask, render_template
from flask import request
import requests
import json

app = Flask(__name__)
app.debug = True


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route("/months")
@app.route("/month", methods=['GET'])
def month():
    # Retrieve the month from the requests, or use 'default' if not provided
    m = request.args.get('month', 'default')

    # Pass the month arg to the render template
    return render_template('months.html', month=m)


if __name__ == '__main__':
    app.run(debug=True)
