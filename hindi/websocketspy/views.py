from django.shortcuts import render
from time import sleep
import cv2
import base64
import numpy as np
from datetime import datetime
import os, io
import time
from time import gmtime, strftime
from PIL import Image
import face_recognition as fc
from .models import AddEmployee
from .forms import AddEmployeeForm, CreateUserForm


path = "images"
images = []
personName = []
mylist = os.listdir(path)
# print(mylist)
encodeList = []

# Create your views here.
def index(request):
    return render(request, 'websocketspy/index.html')

def AddEmployeeView(request):
    if not request.user.is_superuser:
        return render(request, 'employee/superusers_req.html')
    else:
        form = AddEmployeeForm()
        form2 = CreateUserForm()
        if request.method == "POST":
            emp_code = request.POST.get('emp_code')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            post_code = request.POST.get('post_code')
            country = request.POST.get('country')
            dept = request.POST.get('dept')
            picture = request.POST.get('picture')
            dob = request.POST.get('dob')
            father_name = request.POST.get('father_name')
            mother_name = request.POST.get('mother_name')
            marital_status = request.POST.get('marital_status')
            gender = request.POST.get('gender')
            salary_type = request.POST.get('salary_type')
            salary = request.POST.get('salary')
            date_of_joining = request.POST.get('date_of_joining')
            elwp = request.POST.get('elwp')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            office_time = request.POST.get('office_time')
            date_of_leaving = request.POST.get('date_of_leaving')

            print("Password1: ", password1)
            print("Password2: ", password2)

            form = AddEmployeeForm(request.POST, request.FILES)
            form2 = CreateUserForm(request.POST)

            if form.is_valid() and form2.is_valid():
                form.save()
                form2.save()
                print("Form Saved")
                # messages.success(request, "User Added" )
                # redirect('/')
            else:
                # messages.error(request, f"Error. {form.errors}")
                print("Error")
                print(form.errors)

        context = {'form': form, 'form2': form2}
        return render(request, 'websocketspy/add_employee.html', context)
