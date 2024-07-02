from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Registration(models.Model):
    data= [('male', 'Male'),('female', 'Female'),('other', 'Other')]
    data2 = [('Live online', 'Live online'),('Classroom', 'Classroom'),]
    data3 = [('Technopark TVM', 'Technopark TVM'),('Thampanoor TVM', 'Thampanoor TVM'),('Kochi', 'Kochi'),('Nagercoil', 'Nagercoil'),('Online', 'Online'),]
    data4= [('cycling', 'cycling'),('gardening', 'gardening'),('cooking', 'cooking'),('knitting', 'knitting'),]
    full_name=models.CharField(max_length=100) 
    date_of_birth=models.DateField()
    gender = models.CharField(max_length=10,choices=data)
    educational_qualification=models.CharField(max_length=100)
    upload_avatar = models.FileField(upload_to="user_avatar")
    mobile_number=models.IntegerField()
    email=models.EmailField(max_length=254)
    guardians_mobile=models.IntegerField()
    training_mode = models.CharField(max_length=20,choices=data2)
    location = models.CharField(max_length=20,choices=data3)
    guardians_name=models.CharField(max_length=100,blank=True)
    guardians_occupation=models.CharField(max_length=100,blank=True)
    hobbies=models.TextField()
    address=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    pin_zip_code=models.IntegerField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='registration',null=True)


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fees = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SelectedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        course_names = ', '.join(course.name for course in self.courses.all())
        return f"{self.user.username}: [{course_names}]"
    
    
