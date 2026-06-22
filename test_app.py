# test_app.py
from app import get_message, add_numbers

def test_get_message():
    assert get_message() == "Hello from Docker on Windows!"
    print("✅ Message test passed!")

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    print("✅ Addition tests passed!")

def test_add_numbers_edge_cases():
    assert add_numbers(100, 200) == 300
    assert add_numbers(-5, -5) == -10
    print("✅ Edge case tests passed!")

if __name__ == "__main__":
    test_get_message()
    test_add_numbers()
    test_add_numbers_edge_cases()
    print("\n🎉 All tests passed successfully!")