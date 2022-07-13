import json

def test_home(api):
    """Home Page Loads"""
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'Enter the URL you would like to shorten!' in resp.data
