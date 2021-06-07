from django.core.management.base import BaseCommand
import csv
from app.models import Customer
import requests
import json
from app.constants import api_key

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        with open('Customer.csv', 'r') as f:
            csv_file = csv.reader(f, delimiter=',')
            header = next(csv_file)
            for row in csv_file:

                # initializing an empty dictionary for each row
                row_dict = {
                    'name': '',
                    'sale_amount': None,
                    'lattitude': None,
                    'longitude': None,
                    'address': '',
                    'pincode': ''
                }

                # loading the dictionary with the data from the csv
                for i,col in enumerate(row):
                    row_dict[header[i]] = col

                # address = ''
                # pincode = ''
                # response = requests.get('https://maps.googleapis.com/maps/api\
                #                         /geocode/json?latlng=' + \
                #                         str(row_dict['lattitude']) + ',' + \
                #                         str(row_dict['longtitude'])'&key=' + \
                #                         api_key)
                # address_content = json.loads(response.content)
                # row_dict['address'] = address
                # row_dict['pincode'] = pincode
                
                r = Customer(name=row_dict['name'],
                            sale_amount=row_dict['sale_amount'],
                            lattitude=row_dict['lattitude'],
                            longitude=row_dict['longitude'],
                            address=row_dict['address'],
                            pincode=row_dict['pincode'])
                r.save()