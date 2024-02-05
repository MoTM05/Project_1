from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .permissions import IsAdminOrReadOnly
from .serializers import *


class EquipmentAPIList(generics.ListAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAuthenticated, )

class EquipmentAPICreate(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAdminOrReadOnly, )

class EquipmentAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAdminOrReadOnly, )




class OrdersAPIList(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated, )

class OrdersAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAdminOrReadOnly, )

class OrdersAPICreate(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = (IsAdminOrReadOnly, )



class ReportsAPIList(generics.ListAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    #permission_classes = (IsAuthenticated, )

class ReportsAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = (IsAuthenticated, )

class ReportsAPICreate(generics.ListCreateAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer
    permission_classes = (IsAuthenticated, )

# class ReportsViewSet(viewsets.ModelViewSet):
#     queryset = Equipment.objects.all()
#     serializer_class = ReportsSerializer
#
#     @action(methods=['get'], detail=True)
#     def equipment(self, request, pk=None):
#         char = Equipment.objects.get(pk=pk)
#         return Response({'char': [c.name for c in char]})


# class ReportsAPIList(generics.ListCreateAPIView):
#     queryset = Equipment.objects.all()
#     serializer_class = ReportsSerializer
#
#
# class ReportsAPIUpdate(generics.UpdateAPIView):
#     queryset = Equipment.objects.all()
#     serializer_class = ReportsSerializer
#
#
# class ReportsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Equipment.objects.all()
#     serializer_class = ReportsSerializer

# class ReportsAPIView(APIView):
#     def get(self, request):
#         w = Equipment.objects.all()
#         return Response({'Оборудование': ReportsSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = ReportsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Метод PUT недоступен'})
#
#         try:
#             instance = Equipment.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Объект не найден'})
#
#         serializer = ReportsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error': 'Удаление недоступно'})
#         try:
#             instance = Equipment.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Документ не найден'})
#
#         w = Equipment.objects.get(pk=pk)
#         w.delete()
#         return Response({'post': 'Данные удалены.'})




#class ReportsAPIView(generics.ListAPIView):
    #queryset = Equipment.objects.all()
    #serializer_class = ReportsSerializer
