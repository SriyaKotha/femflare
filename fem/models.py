from django.contrib.auth.models import User
from django.db import models

# Create your models here.
GENDER = (
    ("MALE", 'MALE'),
    ("FEMALE", 'FEMALE')
)

YEAR = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5")
)

BRANCH = (
    ("CSE", 'CSE'),
    ("ECE", 'ECE'),
    ("ECM", 'ECM'),
    ("MECH", 'MECH'),
    ("CIVIL", 'CIVIL'),
    ("BT", 'BT'),
    ("BBA", 'BBA'),
    ("EEE", 'EEE'),
    ("BCA", 'BCA'),
    ("LAW", 'LAW'),
    ("MBA", 'MBA'),
    ("HOTEL MANG.", 'HOTEL MANG.'),
    ("FINE ARTS", 'FINE ARTS'),
    ("ARCH.T", 'ARCH.T'),
    ("OTHER", 'OTHER')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, default=999999999)
    college_name = models.CharField(max_length=30, default='KL Vijayawada')
    branch = models.CharField(choices=BRANCH, default='CSE', max_length=20)
    year_of_study = models.TextField(choices=YEAR, max_length=10, default=1)
    gender = models.CharField(choices=GENDER, default='MALE', max_length=6)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Demo(models.Model):
    phone = models.CharField(max_length=10, default=999999999)
