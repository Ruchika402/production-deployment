import pytest
from app import app

def test_add():
    # This creates a test client that simulates browser requests
    client = app.test_client()
    
    # This simulates a GET request to /add?a=2&b=3
    response = client.get('/add?a=2&b=3')
    
    # Check if "2 + 3 = 5" appears in the response
    assert b'2 + 3 = 5' in response.data
    assert response.status_code == 200