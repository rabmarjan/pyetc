# this is python's built-in reference WSGI webserver
# it is highly useful for testing, but there are much
# better deployment options for production
from wsgiref import simple_server

import my_web_framework


def run():
    api = my_web_framework.MyAPI()
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    print("Running at host: ", "127.0.0.1")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
