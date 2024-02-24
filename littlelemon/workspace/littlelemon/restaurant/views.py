from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

'''class bookingview(APIView):
    
    def get(self, request):
        items = Booking.object.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    
class menuview(APIView):
    def post(self, request):
        serrializer = MenuSerializer(data=request.data)
        if serrializer.is_valid():
            serrializer.save()
            return Response({'status':'success', 'data':serializer.data})'''

class MenuItemsView(generics.ListCreateAPIView):   
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]  
        
        