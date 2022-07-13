from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from secrets import token_urlsafe

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)

## Routes *****************************************************************************************
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

@app.route('/link', methods=['Get', 'Post'])
def all_links():
    fns = {"GET": index, "POST": create}
    if request.method == "POST":
        your_url = request.form['link']
        url_id = shorten()
        return render_template('result.html', your_url=your_url, url_id=url_id, title='Result')
    if request.method == "GET":
        # resp, code = fns[request.method](request)
        # return jsonify(resp), code
        pass
    pass

@app.route('/link/<page_id>',  methods=['Get', 'Delete'])
def link_by_id():
    fns = {"GET": index, "DELETE": destroy}
    if request.method == "GET":
        # resp, code = fns[request.method](request)
        # return jsonify(resp), code
        pass
    if request.method == "DELETE":
        # resp, code = fns[request.method](request)
        # return jsonify(resp), code
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

if __name__ == "__main__":
    app.run(debug=True)

## Model ******************************************************************************************
class Links(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    link = db.Column(db.String())

    def __init__(self,link):
        self.link = link
    
    def __repr__(self):
        return f"{self.id} - {self.name}"

## Controllers ************************************************************************************
def index():
    pass

def create():
    pass

def destroy():
    pass

def shorten() -> str:
    ext = token_urlsafe(5)
    if ext in db:
        return shorten()
    else:
        return ext
