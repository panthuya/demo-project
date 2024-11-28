import os
from flask import Flask

# Get the port number from the environment variable or use 5002 as default
port = int(os.environ.get('PORT', 5002))  # Changed `init` to `int` for correct type conversion

# Create a Flask app
app = Flask(__name__)  # Changed `_name_` to `__name__`

# Define a route and handler for the root URL
@app.route('/')
def hello():
    return f'Hello, World! Running on port {port}'  # Fixed the string formatting syntax

# Start the Flask app on the specified port
if __name__ == '__main__':  # Fixed `if__name__` to `if __name__`
    app.run(host='0.0.0.0', port=port)