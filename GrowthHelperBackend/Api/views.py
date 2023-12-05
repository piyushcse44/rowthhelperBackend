from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from InvestApp.serializer import StartupSerializer
from GetInTouchApp.serializer import ContactSerializer,Contact
from InvestApp.models import Startup
from rest_framework.parsers import JSONParser
import io
# Create your views here.

def route_list(request):
    return render(request,'home.html')


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





