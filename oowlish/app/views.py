from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer

@api_view(['GET',])
def get_customer(req,ds,dt):
    cus = Customer.objects.values_list()
    for i in cus:
        print(i)
    return Response('', status=status.HTTP_201_CREATED)

@api_view(['POST',])
def post_customer(req):
    data = req.data
    cus = Customer.objects.values_list()
    for i in cus:
        print(i)
    

    return Response(data, status=status.HTTP_201_CREATED)