# from flask import Flask
# from flask import request
from flask import *
app = Flask(__name__)

@app.route("/")
def hello():
    print(request)
    return Response('a30166a3')


if __name__ == "__main__":
    app.run()
