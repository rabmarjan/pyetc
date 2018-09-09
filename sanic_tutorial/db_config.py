import asyncio
import asyncpg
from asyncpgsa import pg
from pyexcel.cookbook import merge_all_to_a_book
# import pyexcel.ext.xlsx  # needed to support xlsx format, pip install pyexcel-xlsx
import glob
from sanic import Sanic
from sanic.response import json, text
import ujson

app = Sanic()


async def run():
    await pg.init(
        host='127.0.0.1',
        port=5432,
        database='contact_db',
        user='postgres',
        # loop=loop,
        password='odoo',
        min_size=5,
        max_size=10
    )
    # conn = await asyncpg.connect(user='postgres', password='odoo',
    #                              database='contact_db', host='127.0.0.1')
    values = await pg.fetch('''SELECT * FROM employee''')
    # await conn.copy_from_query('''SELECT * FROM employee''', output='file.csv', format='csv')
    # merge_all_to_a_book(glob.glob("file.csv"), "output.xlsx")
    for record in values:
        print(dict(record))
    print(type(record))
    # await pg.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(run())


@app.route("/", methods=["GET", "POST", ])
async def db_response(request):
    # conn = await asyncpg.connect(user='postgres', password='odoo',  database='contact_db', host='127.0.0.1')
    # conn = await asyncpg.connect('postgresql://postgres:odoo@localhost/contact_db')
    pool = await asyncpg.create_pool("postgres://postgres:odoo@localhost:5432/contact_db", min_size=5, max_size=10,
                                     max_inactive_connection_lifetime=60)
    conn = await pool.acquire()
    try:
        values = await conn.fetch('''SELECT * FROM employee''')
    finally:
        await pool.release(conn)
    my_val = {}
    for val in values:
        my_val = val
    return json(dict(my_val), status=200, headers={
        'header': {'responseCode': '200', 'responseMessage': 'Data successfully loaded'},
        'meta': {}})
    # return await file('/home/rose/Pictures/dok.jpg')


if __name__ == "__main__":
    # pass
    app.run('0.0.0.0', port=8000, workers=3)
