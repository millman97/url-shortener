from flask import Flask, jsonify, redirect, render_template, request
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
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

@app.route('/api', methods=['Get', 'Post'], title='All Links')
def all_links():
    fns = {"GET": index, "POST": create}
    if request.method == "POST":
        "link": request.form["link"]
        pass
    if request.method == "GET":
        resp, code = fns[request.method](request)
        return jsonify(resp), code
    pass

@app.route('/api/<page_id>',  methods=['Get', 'Delete'], title='Link:<page_id>')
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
