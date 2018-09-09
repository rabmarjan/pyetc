import numpy as np
import cv2
import time
import requests
import threading
from threading import Thread, Event, ThreadError


class Cam():
    def __init__(self, url):

        self.stream = requests.get(url, stream=True)
        self.thread_cancelled = False
        self.thread = Thread(target=self.run)
        print("camera initialised")

    def start(self):
        self.thread.start()
        print("camera stream started")

    def run(self):
        bytes = b''
        while not self.thread_cancelled:
            try:
                bytes += self.stream.raw.read(1024)
                a = bytes.find(b'\xff\xd8')
                b = bytes.find(b'\xff\xd9')
                if a != -1 and b != -1:
                    jpg = bytes[a:b + 2]
                    bytes = bytes[b + 2:]
                    img = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                    cv2.imshow('cam', img)
                    if cv2.waitKey(1) == 27:
                        exit(0)
            except ThreadError:
                self.thread_cancelled = True

    def is_running(self):
        return self.thread.isAlive()

    def shut_down(self):
        self.thread_cancelled = True
        # block while waiting for thread to terminate
        while self.thread.isAlive():
            time.sleep(1)
        return True


if __name__ == "__main__":
    # url = 'http://192.168.2.1/?action=stream'
    #url = "http://admin:CAM1cam@192.168.3.11:80/cgi-bin/viewer/video.jpg?resolution=640x480"
    url = "https://www.youtube.com/watch?v=QRq6p9s8NVg"
    cam = Cam(url)
    cam.start()
# main.py

# from flask import Flask, render_template, Response
# from video import camstream
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(camstream()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
#
# if __name__ == '__main__':
#     app.run(host='192.168.5.169', debug=True)