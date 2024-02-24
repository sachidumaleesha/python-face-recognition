import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle

path = 'student_images'

images = []
classNames = []mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])