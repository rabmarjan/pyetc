import cv2
import urllib
from urllib.request import urlopen
import numpy as np
import requests
stream = requests.get('http://admin:CAM1cam@192.168.3.11:80/cgi-bin/viewer/video.jpg/?action=stream', stream=True)
bytes = b''
while True:
    bytes += stream.raw.read(1024)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b + 2]
        bytes = bytes[b + 2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('i', i)
        if cv2.waitKey(1) == 27:
            exit(0)