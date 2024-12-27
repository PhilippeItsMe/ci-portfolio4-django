from . import views
from django.urls import path

urlpatterns = [
    path('', views.Business_List.as_view(), name='home'),
]