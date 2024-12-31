from django.shortcuts import render
from django.views import generic
from .models import Pet_Businesse

# Business list view
class Business_List(generic.ListView):
    queryset = Pet_Businesse.objects.all()
    template_name = "pet_businesses/pet_business_list.html"
    context_object_name = "pet_business_list"
    paginate_by = 3

# Business detail view
def pet_business_detail(request, slug):
    queryset = Pet_Businesse.objects.filter(approved=True)
    post = get_object_or_404(queryset, slug=slug)
    context_object_name = "pet_business_detail"

    return render(
        request,
        "pet_businesses/pet_business_detail.html",
        {"pet_business_detail": pet_business_detail},
    )

