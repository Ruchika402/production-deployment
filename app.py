# app.py
def get_message():
    return "Hello from Docker on Windows!"

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(get_message())
    print(f"2 + 3 = {add_numbers(2, 3)}")