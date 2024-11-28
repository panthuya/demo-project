# app.py
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return 'Hello Pan, This is Version2!'

# Define another route for a custom message
@app.route('/about')
def about():
    return 'This is a simple Flask application running on Python 3!'

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
