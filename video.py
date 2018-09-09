import pygame
import pygame.camera
from pygame.locals import *
import random
import string


DEVICE = '/dev/video0'
SIZE = (640, 480)
FILENAME = '/home/rose/Pictures/capture+"' + str(random.random()) + '"+.jpg'


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def camstream():
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(SIZE, 0)
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()
    screen = pygame.surface.Surface(SIZE, 0, display)
    capture = True
    while capture:
        screen = camera.get_image(screen)
       # pygame.image.save(screen, FILENAME+id_generator())
        display.blit(screen, (0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
            elif event.type == KEYDOWN and event.key == K_s:
                pygame.image.save(screen, FILENAME)
    camera.stop()
    pygame.quit()
    return


if __name__ == '__main__':
    camstream()

# import pygame, sys
# import pygame.camera
# from pygame.locals import *
# pygame.init()
# pygame.camera.init()
# screen = pygame.display.set_mode((320,240))
# cam = pygame.camera.Camera("/dev/video0",(320,240))
#
# cam.start()
# while 1:
#     image = cam.get_image()
#     screen.blit(image,(0,0))
#     pygame.display.set_caption(str("TUX PLOT CAM"))
#     pygame.display.update()
#     for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#          sys.exit()

# import cv2

# class VideoCamera(object):
#     def __init__(self):
#         # Using OpenCV to capture from device 0. If you have trouble capturing
#         # from a webcam, comment the line below out and use a video file
#         # instead.
#         self.video = cv2.VideoCapture(0)
#         # If you decide to use video.mp4, you must have this file in the folder
#         # as the main.py.
#         # self.video = cv2.VideoCapture('video.mp4')
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         success, image = self.video.read()
#         # We are using Motion JPEG, but OpenCV defaults to capture raw images,
#         # so we must encode it into JPEG in order to correctly display the
#         # video stream.
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

# import cv2
# import numpy as np
# import cv2
#
# # Load an color image in grayscale
# img = cv2.imread('/home/rose/Pictures/capture.jpg', 0)
# cv2.imwrite("/home/rose/Pictures/capture1.jpg", img)
# #cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
