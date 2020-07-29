# from flask import Flask
# from flask import request
from flask import *
app = Flask(__name__)

@app.route("/", methods = ["POST"])
def hello():
    data = json.loads(request.data)
    if data["type"] == "confirmation":
        return Response('a30166a3',status=200)
    return Response('ok',status=200)


if __name__ == "__main__":
    app.run()
