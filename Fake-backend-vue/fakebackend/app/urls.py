
from django.conf.urls import url, re_path
from django.urls import path
from .views import CustomerView, CustomerDetail

urlpatterns = [
    path('api/v1/contact/', CustomerView.as_view()),
    path('api/v1/contact/<int:id>', CustomerDetail.as_view()),
]