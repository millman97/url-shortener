from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError
import os
from flask_sqlalchemy import SQLAlchemy
from secrets import token_urlsafe

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)

## Routes *****************************************************************************************
# Catch All Redirect to Index.html
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    print("path accessed:", path)
    return render_template('home.html', title='Home')

@app.route('/<page_id>')
def redirect_to_link(page_id):
    the_link = db.session.query(Links).filter_by(uid=page_id).first()
    return redirect(the_link.link, code=302, Response=None)

@app.route('/link', methods=['Get', 'Post'])
def all_links():
    fns = {"GET": index, "POST": create}
    if request.method == "POST":
        return fns[request.method](request)
    if request.method == "GET":
        resp, code = fns[request.method](request)
        return jsonify(resp), code

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
    uid = db.Column(db.String())
    link = db.Column(db.String())

    def __init__(self,link,uid):
        self.link = link
        self.uid = uid
    
    def __repr__(self):
        return f"{self.link}"

    def index(req):
        links = db.session.query(Links).all()
        results = [{
            "id":link.id,
            "uid": link.uid,
            "link": link.link
        } for link in links]
        return results, 200

    def create(req):
        your_url = request.form['link']
        url_id = Links.shorten()
        new_record = Links(your_url, url_id)
        db.session.add(new_record)
        db.session.commit()
        results = {
            "your_url":your_url,
            "url_id":url_id
            }
        return results, 201

    def shorten() -> str:
        links = db.session.query(Links).all()
        ext = token_urlsafe(5)
        if ext in links:
            return Links.shorten()
        else:
            return ext

## Controllers ************************************************************************************
def index(req):
    results = Links.index(req)
    return results, 200

def create(request):
    your_url = request.form['link']
    url_id = shorten()
    new_record = Links(your_url, url_id)
    db.session.add(new_record)
    db.session.commit()
    return render_template('result.html', your_url=your_url, url_id=url_id, title='Result')

## Other Functions ************************************************************************************
def shorten() -> str:
    links = db.session.query(Links).all()
    ext = token_urlsafe(5)
    if ext in links:
        return shorten()
    else:
        return ext
