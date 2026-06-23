from app import app
'''
def test_hello():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello from Docker on Windows!" in response.data
    print("✅ Hello endpoint test passed!")

def test_health():
    response = app.test_client().get('/health')
    assert response.status_code == 200
    print("✅ Health check test passed!")
'''
def test_add():
    response = app.test_client().get('/')
    assert b"2 + 3 = 5" in response.data
    print("✅ Add endpoint test passed!")

if __name__ == "__main__":
    #test_hello()
    #test_health()
    test_add()
    print("\n🎉 All tests passed successfully!")