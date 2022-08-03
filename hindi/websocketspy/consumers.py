from random import randint
import json
from channels.generic.websocket import WebsocketConsumer
from time import sleep
import cv2
import base64
import numpy as np
from datetime import datetime
import os, io
from PIL import Image
from io import StringIO
import face_recognition as fc
# from byte_array import byte_data
import re
from PIL import ImageGrab

import matplotlib.pyplot as plt
from imageio import imread



path = "images"
images = []
personName = []
mylist = os.listdir(path)
# print(mylist)
encodeList = []

for cu_img in mylist:
    current_img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_img)

    personName.append(os.path.splitext(cu_img)[0])

def faceEncodings(images):
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fc.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def MarkAttendance(name):
    with open('atten.csv', 'w+') as f:
        myDateList = f.readlines()
        nameList = []
        for line in myDateList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'{name},{tStr},{dStr}\n')

print("Encoding Completed")
encodeListKnown = faceEncodings(images)

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        if len(text_data) < 10:
            pass
        else:
            def readb64(uri):
                encoded_data = uri.split(',')[1]
                nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                return img


            faces = cv2.resize(readb64(text_data), (640,480))
            
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrentFrame = fc.face_locations(faces)
            encodeCurrentFrame = fc.face_encodings(faces, facesCurrentFrame)

            for encodeFace, faceLocation in zip(encodeCurrentFrame, facesCurrentFrame):
                matches = fc.compare_faces(encodeListKnown, encodeFace)
                print("Matches: ", matches)
                facedis = fc.face_distance(encodeListKnown, encodeFace)

                matchIndex = np.argmin(facedis)

                if matches[matchIndex]:
                    name = personName[matchIndex].upper()
                    print(name)

                    y1, x2, y2, x1 = faceLocation
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

                    MarkAttendance(name)

