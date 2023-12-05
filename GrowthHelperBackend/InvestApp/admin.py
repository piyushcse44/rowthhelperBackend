from django.contrib import admin
from .models import Startup,Competitor,CompanyDocument,Sector

# Register your models here.


admin.site.register(Startup)
admin.site.register(CompanyDocument)
admin.site.register(Competitor)
admin.site.register(Sector)
