from rest_framework import serializers
from .models import ClientTestimonial

class ClientTestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientTestimonial
        fields = '__all__'

