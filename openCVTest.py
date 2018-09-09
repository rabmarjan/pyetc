import numpy as np
import os
# import tensorflow as ts
#
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#
# print("hello")
# err = np.array([[1, 2, 3], [4, 5, 6]])
# print(err)

# hello = ts.constant("Hello, there!")
# sess = ts.Session()
# print(sess.run(hello))

import cv2

print(cv2.__version__)

img = cv2.imread('/home/rose/Pictures/beautiful-pic.jpg', 0)
print(img)

import numpy as np
import cv2

img = cv2.imread('/home/rose/Pictures/beautiful-pic.jpg', 0)
print(img)
