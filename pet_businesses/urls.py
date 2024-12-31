from . import views
from django.urls import path

urlpatterns = [
    path('', views.Business_List.as_view(), name='home'),
    path('<slug:slug>/', views.pet_business_detail, name='pet_business_detiail'),
]