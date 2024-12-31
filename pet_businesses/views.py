from django.shortcuts import render
from django.views import generic
from .models import Pet_Businesse

# Create your views here.
class Business_List (generic.ListView):
    queryset = Pet_Businesse.objects.all()
    template_name = "pet_businesses/pet_business_list.html"
    paginate_by = 3
