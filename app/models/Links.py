from flask import request
from app.database import db
from secrets import token_urlsafe

heroku_url = 'https://url-is-short.herokuapp.com/'

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
        if db.session.query(Links).filter_by(link=your_url).first():
            q = db.session.query(Links).filter_by(link=your_url).first()
            results = {
                "your_url":your_url,
                "url_id":heroku_url + q.uid
                }
            status = 200 
        else:
            url_id = Links.shorten()
            new_record = Links(your_url, url_id)
            db.session.add(new_record)
            db.session.commit()
            results = {
                "your_url":your_url,
                "url_id":heroku_url + url_id
                }
            status = 201
        results['link_total'] = len(db.session.query(Links).all())
        return results, status

    def shorten() -> str:
        links = db.session.query(Links).all()
        ext = token_urlsafe(5)
        if ext in links:
            return Links.shorten()
        else:
            return ext
