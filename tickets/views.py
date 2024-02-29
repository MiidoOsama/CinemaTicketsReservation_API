from django.shortcuts import render
from .serializers import GuestSerializer , MovieSerializer , ReservationSerializer
from django.http.response import JsonResponse
from .models import Guest,Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , filters
# Create your views here.

#1 without REST framework and no model query (FBV)

def no_rest_no_model(request):
    guests =[
        {
            'id' : 1,
            "Name" : "Omar",
            "mobile": 965784320,

        },
        {
            'id':2 ,
            'Name':'Ali',
            'mobile': 965784321,
        }
    ]

    return JsonResponse (guests, safe=False)



#2 without REST framework from model

def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests' : list(data.values('name','mobile'))
    }
    return JsonResponse(response)


#3 FBV
#3.1 GET POST
@api_view(['GET','POST'])
def FBV_List(request):
    #GET
    if  request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests , many=True)
        return Response(serializer.data)
    #POST
    elif request.method=='POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED )
        return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)

#3.1 GET PUT DELETE
@api_view(['GET','PUT', 'DELETE'])
def FBV_pk(request , pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #GET
    if  request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    elif request.method=='PUT':
        serializer = GuestSerializer(guest,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_202_ACCEPTED )
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if  request.method == 'DELETE':
        guest.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
