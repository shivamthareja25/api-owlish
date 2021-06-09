from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import jsontopython, pytojson
import concurrent.futures

@api_view(['GET'])
def get_customer_by_id(req,id):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(getCustomerById, (id))
            data = future.result()
        return Response(data, status=status.HTTP_201_CREATED)
    except:
        return Response('Error', status=400)

@api_view(['GET'])
def get_all_customers(req):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(getCustomers, )
            data = future.result()
        return Response(data, status=status.HTTP_201_CREATED)
    except:
        return Response('Error', status=400)
    
def getCustomers():
    try:
        Cust = Customer.objects.values_list()
        data = pytojson(Cust)
        return data
    except:
        print('Error in Multithreading')

def getCustomerById(id):
    try:
        Cust = Customer.objects.filter(id=id).values()
        data = pytojson(Cust)
        return data
    except:
        print('Error in Multithreading')
    
        # https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY
    
    

