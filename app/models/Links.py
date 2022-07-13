from flask import request
from app.database import db
from secrets import token_urlsafe

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
