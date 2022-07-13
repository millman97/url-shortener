import json

def test_home(api):
    """Home Page Loads"""
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'Enter the URL you would like to shorten!' in resp.data
    
def test_links(api):
    """Home Page Loads"""
    resp = api.get('/', method='GET')
    assert resp.status == '200 OK'
    assert len(resp.data)>1
