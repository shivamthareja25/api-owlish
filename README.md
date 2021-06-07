# rest-api-owlish
1. This project requires is build on Python 3.6.

2. The Custom Django Command the CSV file is "python manage.py readmycsv"
    a.The file should be put in the parent oowlish folder and named Customer.csv.
    b.The Google Maps API key is put inside constants.py

3. The UI based Api documentation can be found at '/swagger'.

4. There are namely 2 GET API's:
    i. GetAllCustomers - It returns the data of all the customers in Json format.
    ii. GetCustomerById - It uses parameter called id(Primary Key). And gives back the data of the  customer with the specific id.

5. In order to run the code in one command, user needs to have python 3.6 installed.
    a. Go to the root folder 
    b. Write in the CLI '. env/bin/activate'
    c. Write 'cd oowlish'
    d. Write 'python manage.py migrate'
    b. Then write 'python manage.py runserver'