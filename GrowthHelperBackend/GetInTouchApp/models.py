from django.db import models

def get_default_startup_pic():
    return 'images/default_startup_pic.jpg'

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    who_are_you = models.CharField(max_length=200)
    email = models.EmailField()
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.full_name} ({self.email})"
    
from django.db import models

class FundRasing(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about_ur_company = models.TextField()
    upload_files = models.FileField(upload_to='',default=get_default_startup_pic)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id} - {self.company_name} ({self.email})"

