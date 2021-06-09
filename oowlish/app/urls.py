from django.urls import path
from . import views

urlpatterns = [
	path('getcustomer/<int:id>', views.get_customer_by_id),
    path('getallcustomers', views.get_all_customers),
]