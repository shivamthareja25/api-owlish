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
                    'address': ''
                }

                # loading the dictionary with the data from the csv
                for i,col in enumerate(row):
                    row_dict[header[i]] = col
                # -------------------------GOOGLE MAPS API--------------------
                response = requests\
                    .get('https://maps.googleapis.com/maps/api/geocode/json?latlng='\
                        + str(row_dict['lattitude']) + ',' + \
                        str(row_dict['longitude']) + '&key=' +\
                        api_key)
                import pdb
                pdb.set_trace()
                address_content = json.loads(response.content)
                row_dict['address'] = \
                    address_content['results'][0]['formatted_address']
                #----------------------------------------------------------
                
                r = Customer(name=row_dict['name'],
                            sale_amount=row_dict['sale_amount'],
                            lattitude=row_dict['lattitude'],
                            longitude=row_dict['longitude'],
                            address=row_dict['address'])
                r.save()