from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/hello/<name>")
async def hello(request, name):
    return json({"name": name})


if __name__ == "__main__":
    app.run("0.0.0.0", port=8000, workers=2)
