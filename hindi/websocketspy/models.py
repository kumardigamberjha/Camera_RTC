from django.db import models

class AttendanceModel(models.Model):
    user_name = models.CharField(max_length=50)
    attendance_time = models.TimeField()
    date = models.DateField()
    late = models.TimeField(blank=True, null=True)
    sal_ded = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ['user_name', 'date']
    
    def __str__(self):
        return self.user_name

class AddEmployee(models.Model):
    # emp_code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    post_code = models.IntegerField()
    
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=30)

    # dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    dept = models.CharField(max_length=30)

    picture = models.ImageField(null=True, blank=True)
    dob = models.DateField()
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    # marital_status = models.ForeignKey(MaritalStatus, on_delete=models.SET_NULL, null=True)
    marital_status = models.CharField(max_length=30)

    # gender = models.ForeignKey(GenderModel, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=30)

    salary_type = models.CharField(max_length=30)
    salary = models.FloatField(blank=True, null=True)
    date_of_joining = models.DateField()
    elwp = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    office_time = models.TimeField()
    date_of_leaving = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name