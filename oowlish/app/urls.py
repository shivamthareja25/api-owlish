from django.urls import path
from . import views

urlpatterns = [
	path('getCustomer/<str:ds>/<str:dt>', views.get_customer),
    path('postCustomer', views.post_customer),
]