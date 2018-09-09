import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
import asyncio

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        http_client = AsyncHTTPClient()
        response = await http_client.fetch("http://prothom-alo.com")
        self.write(response.body)

def make_app():
    return tornado.web.Application([
            (r"/", MainHandler),
             ])

async def fetch_coroutine(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body

#def make_app():
#    return tornado.web.Application([r"/", ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
