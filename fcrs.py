# import cv2
# import numpy as np
# import face_recognition as fc
# import os
# from datetime import datetime
# from vidgear.gears import CamGear
# from vidgear.gears import VideoGear

# path = "images"
# images = []
# personName = []
# mylist = os.listdir(path)
# # print(mylist)

# for cu_img in mylist:
#     current_img = cv2.imread(f'{path}/{cu_img}')
#     images.append(current_img)

#     personName.append(os.path.splitext(cu_img)[0])

# def faceEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = fc.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList

# encodeListKnown = faceEncodings(images)
# print("Encoding Completed")

# #cap = cv2.VideoCapture("http://192.168.1.15:8080/")

# #stream = CamGear(source = 'rtsp://192.168.1.15:8080/',stream_mode=True).start()
# stream = VideoGear(source="https://www.youtube.com/watch?v=_bCJ6RiU36U&t=270s").start()

# def MarkAttendance(name):
#     with open('atten.csv', 'r+') as f:
#         myDateList = f.readlines()
#         nameList = []
#         for line in myDateList:
#             entry = line.split(',')
#             nameList.append(entry[0])

#         if name not in nameList:
#             time_now = datetime.now()
#             tStr = time_now.strftime('%H:%M:%S')
#             dStr = time_now.strftime('%d/%m/%Y')
#             f.writelines(f'{name},{tStr},{dStr}\n')

# while True:
#     frame = stream.read()
#     faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
#     faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

#     facesCurrentFrame = fc.face_locations(faces)
#     encodeCurrentFrame = fc.face_encodings(faces, facesCurrentFrame)

#     for encodeFace, faceLocation in zip(encodeCurrentFrame, facesCurrentFrame):
#         matches = fc.compare_faces(encodeListKnown, encodeFace)
#         facedis = fc.face_distance(encodeListKnown, encodeFace)

#         matchIndex = np.argmin(facedis)

#         if matches[matchIndex]:
#             name = personName[matchIndex].upper()
#             print(name)

#             y1, x2, y2, x1 = faceLocation
#             y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
#             cv2.rectangle(frame, (x1, y1), (x2, y2 ), (0,255,0), 3)
#             cv2.rectangle(frame, (x1, y2-35), (x2, y2 ), (0,255,0), cv2.FILLED)

#             cv2.putText(frame, name, (x1 + 6, y2-6), cv2.FONT_ITALIC, 1, (255, 0, 15), 2)
#             MarkAttendance(name)

#     cv2.imshow("Camera: ", frame)
#     if cv2.waitKey(10) == 13:
#         break

# #cap.release()
# cv2.destroyAllWindows()


