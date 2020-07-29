from flask import *
app = Flask(__name__)

@app.route("/", methods = ["POST"])
def hello():
    data = json.loads(request.data)
    if data["type"] == "confirmation":
        return Response('',status=200)
    print(data)
    return Response('ok',status=200)


if __name__ == "__main__":
    app.run()
