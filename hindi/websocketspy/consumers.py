# from random import randint
# import json
# from channels.generic.websocket import WebsocketConsumer
# from time import sleep
# import cv2
# import base64
# import numpy as np
# from datetime import datetime
# import os, io
# import time
# from time import gmtime, strftime
# import face_recognition as fc


# path = "images"
# images = []
# personName = []
# mylist = os.listdir(path)
# # print(mylist)
# time_now = datetime.now()
# in_time = time_now.strftime('%H:%M:%S')
# in_date = time_now.strftime("%Y-%m-%d")
# # last_date = 
# user_datas = []
# user_list = []
# date_list = {}


# def faceEncodings(images):
#     encodeList = []
#     for img in images:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = fc.face_encodings(img)[0]
#         encodeList.append(encode)
#     return encodeList

# encodeListKnown = faceEncodings(images)
# print("Encoding Completed")


# for cu_img in mylist:
#     current_img = cv2.imread(f'{path}/{cu_img}')
#     images.append(current_img)

#     personName.append(os.path.splitext(cu_img)[0])


# class WSConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()

#     def receive(self, text_data):
#         if len(text_data) < 10:
#             pass
#         else:
#             def readb64(uri):
#                 encoded_data = uri.split(',')[1]
#                 nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
#                 img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#                 return img

#             faces = cv2.resize(readb64(text_data), (640,480))

#             faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

#             facesCurrentFrame = fc.face_locations(faces)
#             encodeCurrentFrame = fc.face_encodings(faces, facesCurrentFrame)

#             for encodeFace, faceLocation in zip(encodeCurrentFrame, facesCurrentFrame):
#                 matches = fc.compare_faces(encodeListKnown, encodeFace)
#                 print("Matches: ", matches)
#                 facedis = fc.face_distance(encodeListKnown, encodeFace)

#                 matchIndex = np.argmin(facedis)

#                 if matches[matchIndex]:
#                     name = personName[matchIndex].upper()
#                     print(name)
#                     self.send("Hello")

#                     time_now = datetime.now()
#                     in_time = time_now.strftime('%H:%M:%S')
#                     in_date = time_now.strftime("%Y-%m-%d")
                    
#                     user_name = name
#                     attendance_time = in_time
#                     date = in_date

#                     form = AttendanceModel(user_name = user_name, attendance_time = attendance_time, date = date)
#                     form.save()
#                     print("This form has been Saved")
#                     y1, x2, y2, x1 = faceLocation
#                     y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

#                     # MarkAttendance(name)







###############################################################################################

###############################################################################################


from platform import system_alias
from random import randint
import json
from django.shortcuts import render, redirect
from math import ceil

from channels.generic.websocket import WebsocketConsumer
from time import sleep
import cv2
import base64
import numpy as np
from datetime import datetime
from datetime import date
import os, io
import time
from time import gmtime, strftime
import face_recognition as fc
from channels.exceptions import StopConsumer
from .models import AttendanceModel, AddEmployee
from django.contrib import messages


path = "images"
images = []
personName = []
mylist = os.listdir(path)
# print(mylist)
time_now = datetime.now()
in_time = time_now.strftime('%H:%M:%S')
in_date = time_now.strftime("%Y-%m-%d")
# last_date = 
user_datas = []
user_list = []
date_list = {}

for cu_img in mylist:
    current_img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_img)

    personName.append(os.path.splitext(cu_img)[0])

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fc.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = faceEncodings(images)
print("Encoding Completed")


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

            faces = cv2.resize(readb64(text_data),(640, 480))
            faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            facesCurrentFrame = fc.face_locations(faces)
            encodeCurrentFrame = fc.face_encodings(faces, facesCurrentFrame)

            for encodeFace, faceLocation in zip(encodeCurrentFrame, facesCurrentFrame):
                matches = fc.compare_faces(encodeListKnown, encodeFace)
                facedis = fc.face_distance(encodeListKnown, encodeFace)

                matchIndex = np.argmin(facedis)

                if matches[matchIndex]:
                    name = personName[matchIndex].upper()
                    print(name)

                    time_now = datetime.now()
                    in_time = time_now.strftime('%H:%M:%S')
                    in_date = time_now.strftime("%Y-%m-%d")

                    # user_name = name
                    attendance_time = in_time
                    dates = in_date

                    last_attendance = AttendanceModel.objects.filter(user_name = name)[:1][::-1]
                    arr = []

                    data = AttendanceModel.objects.filter(date = date.today()).order_by('id')
                    # ss = serializers.serialize('json', data)


                    for i in last_attendance:
                        datesss = i.date
                        
                        if name not in arr:
                            if name == "ASHISH":
                                office_time = datetime.strptime('11:00:00',"%H:%M:%S")
                                slate = ""
                                if datetime.strptime(attendance_time,"%H:%M:%S") > office_time:
                                    slate = datetime.strptime(attendance_time,"%H:%M:%S") - office_time
                                print(datetime.strptime(attendance_time,"%H:%M:%S"))
                                
                                b = str(slate)
                                hr = int(b[0:1])
                                min = int(b[2:4])
                                print("late: ", slate)

                                emp = AddEmployee.objects.all()
                                ss = name.capitalize()
                                salary = 0
                                for i in emp:
                                    x = i.name.split(" ")[0]
                                    sd = x.capitalize()
                                    if ss == sd:
                                        salary = i.salary

                                # print("hr: ", hr)
                                # print("min: ", min)
                                # per_day = salary / 30
                                # per_hour = (per_day / 9) * (9 - hr) 
                                # per_min = (per_hour / 60) * (60 - min)

                                # print("per_day: ", per_day) 
                                # print("per_hour: ", per_hour) 
                                # print("per_min: ", per_min) 

                                # print("Total_deduct: ", per_day/per_hour/per_min)
                                sal_deds = (((((salary/30)/9)*(9-hr))/60)*(60-min))
                                today_sal_deds = ceil(sal_deds)
                                # print("Sal Deduction: ", sal_deds)

                                form = AttendanceModel(user_name = name, attendance_time = attendance_time, date = date.today(), late = str(datetime.strptime(attendance_time,"%H:%M:%S") - office_time), sal_ded = today_sal_deds)
                                mod = AttendanceModel.objects.filter(user_name = name, date = date.today()).exists()
                                if mod == True:
                                    self.send(f"Attendance for {name} Already Done")
                                    
                                else:
                                    form.save()
                                    self.send(f"Attendance for {name} Done")
                                    return redirect('/face_detection/')
                            else:
                                office_time = datetime.strptime('09:35:00',"%H:%M:%S")
                                slate = ""
                                if datetime.strptime(attendance_time,"%H:%M:%S") > office_time:
                                    slate = datetime.strptime(attendance_time,"%H:%M:%S") - office_time
                                # print(attendance_time)

                                b = str(slate)
                                hr = int(b[0:1])
                                min = int(b[2:4])
                                # print("late: ", slate)

                                # print("hr: ", hr)
                                # print("min: ", min)
                                emp = AddEmployee.objects.all()
                                ss = name.capitalize()
                                salary = 0
                                for i in emp:
                                    x = i.name.split(" ")[0]
                                    sd = x.capitalize()
                                    if ss == sd:
                                        salary = i.salary

                                # sal_deds = (salary/30/(9*(9-hr))/(60*(60-min)))
                                sal_deds = (((((salary/30)/9)*(9-hr))/60)*(60-min))

                                per_day = salary / 30
                                per_hour = (per_day / 9) * (9 - hr) 
                                per_min = (per_hour / 60) * (60 - min)

                                # print("per_day: ", per_day) 
                                # print("per_hour: ", per_hour) 
                                # print("per_min: ", per_min) 

                                # print("Total_deduct: ", per_day/per_hour/per_min)
                                # print("Sal Deduction: ", sal_deds)
                                today_sal_deds = ceil(sal_deds)
                                # print("Late: ", datetime.strptime(attendance_time,"%H:%M:%S") > office_time, datetime.strptime(attendance_time,"%H:%M:%S") - office_time)
                                form = AttendanceModel(user_name = name, attendance_time = attendance_time, date = date.today(), late = str(datetime.strptime(attendance_time,"%H:%M:%S") - office_time), sal_ded = today_sal_deds)
                                mod = AttendanceModel.objects.filter(user_name = name, date = date.today()).exists()
                                if mod == True:
                                    self.send(f"Attendance for {name} Done")
                                    
                                else:
                                    form.save()
                                    self.send(f"Attendance for {name} Done")
                                    return redirect('/face_detection/')


                        if name in arr and i.date == date.today():
                            data = f"{name} Already Done..."

                        if name in arr and date.today() < i.date:
                            if name == "ASHISH":
                                office_time = datetime.strptime('11:00:00',"%H:%M:%S")
                                slate = ""
                                if datetime.strptime(attendance_time,"%H:%M:%S") > office_time:
                                    slate = datetime.strptime(attendance_time,"%H:%M:%S") - office_time
                                print(attendance_time)
                                
                                b = str(slate)
                                hr = int(b[0:1])
                                min = int(b[2:4])
                                # print("late: ", slate)

                                # print("hr: ", hr)
                                # print("min: ", min)
                                # per_day = salary / 30
                                # per_hour = (per_day / 9) * (9 - hr) 
                                # per_min = (per_hour / 60) * (60 - min)

                                # print("per_day: ", per_day) 
                                # print("per_hour: ", per_hour) 
                                # print("per_min: ", per_min) 

                                # print("Total_deduct: ", per_day/per_hour/per_min)
                                emp = AddEmployee.objects.all()
                                ss = name.capitalize()
                                salary = 0
                                for i in emp:
                                    x = i.name.split(" ")[0]
                                    sd = x.capitalize()
                                    if ss == sd:
                                        salary = i.salary

                                # sal_deds = (salary/30/(9*(9-hr))/(60*(60-min)))
                                sal_deds = (((((salary/30)/9)*(9-hr))/60)*(60-min))

                                print("Sal Deduction: ", sal_deds)
                                print("late: ", slate)
                                today_sal_deds = ceil(sal_deds)

                                # print("Late: ",  datetime.strptime(attendance_time,"%H:%M:%S") > office_time, datetime.strptime(attendance_time,"%H:%M:%S") - office_time)
                                form = AttendanceModel(user_name = name, attendance_time = attendance_time, date = date.today(), late = str(datetime.strptime(attendance_time,"%H:%M:%S") - office_time), sal_ded = today_sal_deds)
                                mod = AttendanceModel.objects.filter(user_name = name, date = date.today()).exists()
                                if mod == True:
                                    self.send(f"Attendance for {name} Done")

                                else:
                                    form.save()
                                    return redirect('/face_detection/')


                            else:
                                office_time = "9:35:00"
                                slate = ""
                                if datetime.strptime('09:35:00',"%H:%M:%S") > office_time:
                                    slate =  datetime.strptime('09:35:00',"%H:%M:%S") - office_time
                                print(attendance_time)
                                
                                b = str(slate)
                                hr = int(b[0:1])
                                min = int(b[2:4])

                                # print("hr: ", hr)
                                # print("min: ", min)
                                # print("late: ", slate)
                                emp = AddEmployee.objects.all()
                                ss = name.capitalize()
                                salary = 0
                                for i in emp:
                                    x = i.name.split(" ")[0]
                                    sd = x.capitalize()
                                    if ss == sd:
                                        salary = i.salary

                                sal_deds = (((((salary/30)/9)*(9-hr))/60)*(60-min))

                                today_sal_deds = ceil(sal_deds)

                                form = AttendanceModel(user_name = name, attendance_time = attendance_time, date = date.today(), late = str(datetime.strptime(attendance_time,"%H:%M:%S") - office_time), sal_ded = today_sal_deds)

                                mod = AttendanceModel.objects.filter(user_name = name, date = date.today()).exists()
                                if mod == True:
                                    pass
                                else:
                                    form.save()
                                    return redirect('/face_detection/')
                            
                        else:
                            data = f"Attendance for {name} Done..."
                            self.send(data)
                            
                    y1, x2, y2, x1 = faceLocation
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4

        cv2.destroyAllWindows()

    def websocket_disconnect(self, event):
        print('websocket disconnected...', event)  
        raise StopConsumer()
