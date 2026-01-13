from flask import Flask

app = Flask(__name__)

# This part fixes the error by creating a "Home" page
@app.route('/')
def home():
    return "Hello! Flask is working."

if __name__ == '__main__':
    app.run(debug=True)