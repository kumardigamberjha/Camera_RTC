from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="mark-attendance-index"),
    path('out-attendance/', views.index, name="mark-Out-attendance"),
    path('add_employee/', views.AddEmployeeView, name="add_employee"),
    path('show-attendance/', views.showAttendanceView, name="show-attendance"),
]
