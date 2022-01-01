from django.shortcuts import render
from rest_framework.decorators import api_view #Browser bassed api view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import authentication_classes,permission_classes

# Create your views here.
@api_view(['GET','POST','PUT','PATCH','DELETE']) #All allowed methods
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def Review_api(request,pk=None):
    #GET METHOD
    if request.method=='GET':
        id = pk
        if id is not None:
            try:
                record = Review.objects.get(id=id)
                serializer = ReviewSerializer(record)
                return Response(serializer.data,status=status.HTTP_200_OK)
            except:
                return Response({'msg':'Record Not found'},status=status.HTTP_404_NOT_FOUND)

        record = Review.objects.all()
        serializer = ReviewSerializer(record, many=True)
        return Response(serializer.data)

    #POST METHOD
    if request.method=="POST":
        serializer = ReviewSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Created Successfully!'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)
    
    #PUT METHOD
    if request.method=='PUT':
        id = pk
        record = Review.objects.get(id=id)
        serializer = ReviewSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Record Updated Successfully!'},status=status.HTTP_202_ACCEPTED)
        return Response({'msg':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)

    #PATCH METHOD
    if request.method=='PATCH':
        id = pk
        record = Review.objects.get(id=id)
        serializer = ReviewSerializer(record,data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Record Updated Successfully!'},status=status.HTTP_202_ACCEPTED)
        return Response({'msg':serializer.errors},status=status.HTTP_406_NOT_ACCEPTABLE)

    #DELETE METHOD
    if request.method=='DELETE':
        id = pk
        target_record = Review.objects.get(id=id)
        target_record.delete()
        return Response({'msg':'Deleted Successfully!'})


