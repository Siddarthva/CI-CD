from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Flask app in Docker!</h1>"

app.run(host='0.0.0.0', port=5000)



#docker build -t flask-web-app .

#docker run -d -p 8081:5000 --name flask-container flask-web-app


#For jenkins pipeline, use the following command:
# Remove the existing Docker container named 'flask-container' if it exists
#   docker rm --force flask-container || true

# Build a new Docker image with the tag 'flask-web-app' from the current directory
#   docker build -t flask-web-app .

# Run a new Docker container from the image 'flask-web-app'
# It will run in detached mode (-d), map host port 8081 to container port 5000 (Flask default), and name the container 'flask-container'
#   docker run -d -p 8081:5000 --name=flask-container flask-web-app