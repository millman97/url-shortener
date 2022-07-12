from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Catch All Redirect to Index.html
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    print("path accessed:", path)
    return render_template('home.html', title='Home')

@app.route('/<page_id>')
def redirect_to_link():
    pass
# need handling for incorrect id

@app.route('/api',  methods=['Get', 'Post'])
def all_links():
    pass

@app.route('/api/<page_id>',  methods=['Get', 'Delete'])
def link_by_id():
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
