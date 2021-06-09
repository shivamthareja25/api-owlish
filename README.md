# rest-api-owlish
1. This project is build on Python 3.6.

2. The Custom Django Command the CSV file is "python manage.py readmycsv" a.The file should be put in the parent oowlish folder and named Customer.csv. b.The Google Maps API key is put inside constants.py - Please update it with yours. It is confined to a quota of 500 Calls per day.

3.The UI based Api documentation can be found at '/swagger'.

4.There are namely 2 GET API's: i. GetAllCustomers - It returns the data of all the customers in Json format. ii. GetCustomerById - It uses parameter called id(Primary Key). And gives back the data of the customer with the specific id.

For configuration:
1. Add your IP address in the allowed hosts lists inside settings.py
2. Configure your own database in the settings.py
3. In the constants file. Make sure to add your Google Maps API key. As mine is limited to 500 API calls per day.

The code can be executed in 2 ways ( Docker, usual way):
i. Install Docker on your OS. Then write the following commands. 
    a. docker load < oowlish.docker.tar.
    b. docker-compose up
ii. Manually
    a. Activate the virtual environment with the command . env/bin/activate
    b. cd oowlish
    c. python manage.py runserver
