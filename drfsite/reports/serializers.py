import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


#class ReportsModel:
    #def __init__(self, name, characteristic):
        #self.name = name
        #self.characteristic = characteristic


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ('__all__')


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ('__all__')


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ('__all__')



#def encode():
    #model = ReportsModel('Name: Pushka', 'Characteristic: Strashnaya')
    #model_sr = ReportsSerializer(model)
    #print(model_sr.data, type(model_sr.data), sep='\n')
    #json = JSONRenderer().render(model_sr.data)
    #print(json)


#def decode():
    #stream = io.BytesIO(b'{"name":"Name: Pushka","characteristic":"Characteristic: Strashnaya"}')
    #data = JSONParser().parse(stream)
    #serializer = ReportsSerializer(data=data)
    #serializer.is_valid()
    #print(serializer.validated_data)