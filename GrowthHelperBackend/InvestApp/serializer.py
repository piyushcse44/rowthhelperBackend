from rest_framework import serializers
from InvestApp.models import Sector,Startup

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['sector']

class StartupSerializer(serializers.ModelSerializer):
    sector = SectorSerializer(many=True)  # Use the SectorSerializer for the ManyToManyField

    class Meta:
        model = Startup
        fields = '__all__'

    def create(self, validated_data):
        sectors_data = validated_data.pop('sector')
        startup = Startup.objects.create(**validated_data)

        # Create and add Sector instances to the startup
        for sector_data in sectors_data:
            sector, created = Sector.objects.get_or_create(**sector_data)
            startup.sector.add(sector)

        return startup

    def update(self, instance, validated_data):
        sectors_data = validated_data.pop('sector')
        
        # Update the Startup instance
        instance.start_up_name = validated_data.get('start_up_name', instance.start_up_name)
        # Update other fields as needed

        # Clear existing sectors and add new ones
        instance.sector.clear()
        for sector_data in sectors_data:
            sector, created = Sector.objects.get_or_create(**sector_data)
            instance.sector.add(sector)

        instance.save()
        return instance
