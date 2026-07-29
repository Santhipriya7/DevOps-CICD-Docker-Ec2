from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1> My First DevOps Project</h1>
    <h2>CI/CD Pipeline using Docker & AWS EC2</h2>
    <p>This is a simple Flask application that demonstrates a CI/CD pipeline using Docker and AWS EC2.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

