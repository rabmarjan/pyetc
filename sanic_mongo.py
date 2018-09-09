import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
from motor.motor_asyncio import AsyncIOMotorClient

from sanic import Sanic
from sanic.response import json
from sanic import Blueprint

bp = Blueprint('my_blueprint')

app = Sanic(__name__)
app.blueprint(bp)


@bp.listener('after_server_start')
async def setup_dbconn(app, loop):
    mongo_connection = AsyncIOMotorClient(host='localhost', port=27017)
    global contacts
    contacts = mongo_connection.mydatabase.contacts


@app.route("/")
async def list(request):
    data = await contacts.find().to_list(20)
    for x in data:
        x['id'] = str(x['_id'])
        del x['_id']
    return json(data)


# @app.route("/new") was giving error that POST is not allowed.
@app.route('/new', methods=['POST'])
async def new(request):
    contact = request.json
    insert = await contacts.insert_one(contact)
    return json({"inserted_id": str(insert.inserted_id)})


# loop = asyncio.get_event_loop() has to be commented as get_event_loop() is used inside sanic

app.run(host="0.0.0.0", port=8000, workers=3, debug=True)
