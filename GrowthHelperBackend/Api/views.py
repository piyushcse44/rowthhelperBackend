from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from InvestApp.serializer import StartupSerializer,Startup
from GetInTouchApp.serializer import ContactSerializer,Contact
from testimonialsApp.serializer import ClientTestimonial,ClientTestimonialSerializer
from rest_framework.parsers import JSONParser
import io
# Create your views here.

@api_view(['GET'])
def route_list(request):
    api_list = {
        'startup/' : 'Get all startup details',
        'contact-us/' : 'post all contact form',
        'testimonial/' : 'post all testimonial of client',
    }

    return Response(api_list)


@api_view(['GET'])
def get_startup(request):
    startup_query = Startup.objects.all()
    startup_serializer = StartupSerializer(startup_query,many=True)
    startup_data = startup_serializer.data
    return Response(startup_data)


@api_view(['GET','POST'])
def contact_us(request):
    contact_query = Contact.objects.all()
    contact_query = ContactSerializer(contact_query,many=True)
    
    if request.method == 'POST':

        try:
            
            json_input = request.body
            stream = io.BytesIO(json_input)
            parsed_data = JSONParser().parse(stream)
            serializer = ContactSerializer(data=parsed_data)
            if serializer.is_valid():
                serializer.save()
                data ={
                    'success':True,
                    'msg': "successfully saved",
                }
                return Response(data)
            else:
                data ={
                    'success':False,
                    'msg': "Enter a Valid EmailId",
                }                
                return Response(data)

        except Exception:
            return Response("Error occurs")



    return Response(contact_query.data)



@api_view(['GET','POST'])
def testimonial(request):
    contact_query = ClientTestimonial.objects.all()
    contact_query = ClientTestimonialSerializer(contact_query,many=True)
    
    if request.method == 'POST':

        try:
            
            json_input = request.body
            stream = io.BytesIO(json_input)
            parsed_data = JSONParser().parse(stream)
            serializer = ClientTestimonialSerializer(data=parsed_data)
            if serializer.is_valid():
                serializer.save()
                data ={
                    'success':True,
                    'msg': "successfully saved",
                }
                return Response(data)
            else:
                data ={
                    'success':False,
                    'msg': "Enter a Valid EmailId",
                }                
                return Response(data)

        except Exception:
            return Response("Error occurs")



    return Response(contact_query.data)






