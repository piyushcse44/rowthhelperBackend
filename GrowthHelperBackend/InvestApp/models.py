from django.db import models
from InvestApp import const
import uuid


def get_default_startup_pic():
    return 'images/default_startup_pic.jpg'

def get_default_logo():
    return 'images/default_logo.jpg'

class Sector(models.Model):
    sector = models.CharField(max_length=200,choices=const.SECTOR_CHOICES)

    def __str__(self):
        return self.sector

class Startup(models.Model):
    id = models.IntegerField(primary_key=True)
    uniqueid = models.CharField(max_length=20)
    start_up_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    start_up_pic = models.ImageField(upload_to='images', default=get_default_startup_pic)
    logo = models.ImageField(upload_to='images', default=get_default_logo)
    about_startup_long = models.TextField()
    about_startup_points = models.TextField()
    about_startup_short = models.CharField(max_length=255)
    sector = models.ManyToManyField(Sector)
    tech = models.TextField()
    competitors = models.TextField()
    min_investment = models.IntegerField()
    amount_raised = models.FloatField()
    total_investor = models.IntegerField()
    status_percentage = models.FloatField()
    market_value = models.IntegerField()
    revenue = models.IntegerField()
    state = models.CharField(max_length=255)
    valuation_amount = models.IntegerField()
    funding_goal = models.IntegerField()
    type_of_instrument = models.CharField(max_length=255)
    is_live = models.BooleanField()
    deadline = models.DateField()
    promo_code = models.CharField(max_length=255, null=True, blank=True)
    custom_sections = models.TextField()
    
    def __str__(self):
        return self.start_up_name

class Competitor(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='Competitors')
    start_up_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='images', default=get_default_logo)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    sector = models.ManyToManyField(Sector)
    employee_strength = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.start_up_name

class CompanyDocument(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='company_documents')
    name = models.CharField(max_length=255)
    file_url = models.ImageField(upload_to='documents', default='documents/default_document.jpg')

    def __str__(self):
        return self.name
    
    
