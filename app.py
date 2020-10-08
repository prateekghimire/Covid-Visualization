from flask import Flask,render_template,url_for,request,redirect, make_response
import json
import time
from flask import Flask, render_template, make_response
from generatenumbers import *
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    data = [time.time() * 1000, totalcase(), totaldeath()]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


"""if __name__ == "__main__":
    app.run(debug=True,port=0000)"""
