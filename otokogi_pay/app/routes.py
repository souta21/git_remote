from flask import render_template, request, jsonify
from app import app
from app.seisan import seisan

@app.route('/', methods=['GET', 'POST'])
def index():

    return render_template('index.html')

@app.route('/kingakunyuuryoku.html')
def kingakunyuuryoku():

    if request.method == 'POST':
        pay_dict = request.get_json()
        concequence = seisan(pay_dict)
        return jsonify({"payment":concequence})

    return render_template('kingakunyuuryoku.html')