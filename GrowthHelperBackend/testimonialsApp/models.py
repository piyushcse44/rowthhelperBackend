from django.db import models

# Create your models here.



from django.db import models

def get_default_startup_pic():
    return 'images/default_startup_pic.jpg'

class ClientTestimonial(models.Model):
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    client_pic = models.ImageField(default=get_default_startup_pic,upload_to="images/")
    client_type = models.CharField(max_length=255)
    client_designation = models.CharField(max_length=255)
    client_rating = models.DecimalField(max_digits=3,decimal_places=1)
    client_opinion_heading = models.CharField(max_length=255)
    client_opinion = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.client_name} ({self.client_type})"
