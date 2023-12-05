from django.urls import path
from .views import route_list,get_startup,contact_us


urlpatterns = [
    path('',route_list,name="route_list"),
    path('startup',get_startup,name='get_startup'),
    path('contact-us',contact_us,name='contact_us'),
    
]

