import json
import random
import string

def test_home(api):
    """Test Home Page Loads"""
    resp = api.get('/')
    assert resp.status == '200 OK'
    assert b'Enter the URL you would like to shorten!' in resp.data
    
def test_links(api):
    """Test Return All Links Route"""
    resp = api.get('/link', method='GET')
    assert resp.status == '200 OK'
    assert b'link' in resp.data
    assert len(resp.data)>1

def test_generate_link(api):
    """Test Create Link Route"""
    random_seqeuence = string.ascii_lowercase + string.digits
    random_string = random.choices(random_seqeuence, k=6)
    random_string = "".join(random_string)
    resp = api.post('/link', data={"link": random_string})
    print(resp.status)
    assert resp.status == '200 OK'
    assert b'Shortened' in resp.data
