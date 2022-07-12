from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/<int:page_id>')
def redirect_to_link():
    pass

@app.route('/api',  methods=['Get', 'Post'])
def get_all_links():
    pass

@app.route('/api/<int:page_id>',  methods=['Get'])
def get_link():
    pass

@app.errorhandler(NotFound)
def handle_404(err):
    return render_template('errors/404.html', title='Oops!'), 404

@app.errorhandler(BadRequest)
def handle_405(err):
    return render_template('errors/405.html', title='Oops!'), 405

@app.errorhandler(InternalServerError)
def handle_500(err):
    return render_template('errors/500.html', title='Oops!'), 500
