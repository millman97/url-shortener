from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.errorhandler(NotFound)
def handle_404(err):
    return render_template('errors/404.html', title='Oops!'), 404

@app.errorhandler(BadRequest)
def handle_405(err):
    return render_template('errors/405.html', title='Oops!'), 405

@app.errorhandler(InternalServerError)
def handle_500(err):
    return render_template('errors/500.html', title='Oops!'), 500
