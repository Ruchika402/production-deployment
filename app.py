from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Add Numbers API!"

# This is the route the test is trying to access
@app.route('/add')
def add_numbers():
    # Get parameters from URL query string
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    
    if a is None or b is None:
        return "Missing parameters", 400
    
    result = a + b
    return f"{a} + {b} = {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)