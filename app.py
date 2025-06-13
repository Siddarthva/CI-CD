from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Flask app in Docker!</h1>"

app.run(host='0.0.0.0', port=5000)
