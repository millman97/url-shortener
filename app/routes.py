from app import app
from app.database import db
from flask import jsonify, redirect, render_template, request
from app.controllers import index, create
from app.models import Links
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

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
        resp, code = fns[request.method](request)
        print(resp)
        return render_template(
            'result.html', 
            your_url=resp[0]['your_url'], 
            url_id=resp[0]['url_id'], 
            link_total=resp[0]['link_total'], 
            title='Result'
            )
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


