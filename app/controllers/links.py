from app.models import Links

def index(req):
    results = Links.index(req)
    return results, 200

def create(req):
    results = Links.create(req)
    return results, 201
