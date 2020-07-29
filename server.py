from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    print(request)
    return "a30166a3"

if __name__ == "__main__":
    app.run()
