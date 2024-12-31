from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .models import Pet_Businesse
from .forms import Pet_Businesses_Form


# Business list view
class Business_List(generic.ListView):
    queryset = Pet_Businesse.objects.all()
    template_name = "pet_businesses/pet_business_list.html"
    context_object_name = "pet_business_list"
    paginate_by = 3

# Business detail view

@login_required
def pet_business_detail(request, slug):
    # Retrieve the specific Pet_Businesse object
    post = get_object_or_404(Pet_Businesse.objects.filter(approved=True), slug=slug)

    if request.method == "POST":
        pet_businesses_form = Pet_Businesses_Form(data=request.POST)
        if pet_businesses_form.is_valid():
            pet_business = pet_businesses_form.save(commit=False)
            pet_business.author = request.user  # Ensure the user is logged in
            pet_business.save()
            messages.success(
                request, "Pet business submitted and awaiting approval."
            )
            return render(
                request,
                "pet_businesses/pet_business_detail.html",
                {"pet_business_detail": post, "pet_businesses_form": Pet_Businesses_Form()},
            )
    else:
        pet_businesses_form = Pet_Businesses_Form()

    return render(
        request,
        "pet_businesses/pet_business_detail.html",
        {
            "pet_business_detail": post,
            "pet_businesses_form": pet_businesses_form,
        },
    )




"""

from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Pet_Businesse
from .forms import Pet_Businesses_Form


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

    if request.method == "POST":
        pet_businesses_form = Pet_Businesses_Form(data=request.POST)
    if pet_businesses_form.is_valid():
        pet_business = pet_businesses_form.save(commit=False)
        pet_business.author = request.user
        pet_business.post = post
        pet_business.save()
        messages.add_message(
        request, messages.SUCCESS,
        'Pet business submitted and awaiting approval'
    )

    pet_businesses_form = Pet_Businesses_Form()

    return render(
        request,
        "pet_businesses/pet_business_detail.html",
        {"pet_business_detail": post,
         "pet_businesses_form":pet_businesses_form},
    )
"""