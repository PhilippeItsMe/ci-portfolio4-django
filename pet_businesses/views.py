from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .models import Pet_Businesse, Comment
from .forms import Comment_Form


# Business list view

class Business_List(generic.ListView):
    queryset = Pet_Businesse.objects.all()
    template_name = "pet_businesses/pet_business_list.html"
    context_object_name = "pet_business_list"
    paginate_by = 3


# Business detail view

def pet_business_detail(request, slug):
    
    post = get_object_or_404(Pet_Businesse.objects.filter(approved=True), slug=slug)

    if request.method == "POST":
        comment_form = Comment_Form(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user  # Ensure the user is logged in
            comment.post = post
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting approval."
            )
            return render(
                request,
                "pet_businesses/pet_business_detail.html",
                {"pet_business_detail": post, "comment_form": Comment_Form()},
            )
        else:
            print(comment_form.errors)  # Debugging: Print form errors to the console
            messages.error(request, "There was an error with your submission.")
    else:
        comment_form = Comment_Form()
     

    return render(
        request,
        "pet_businesses/pet_business_detail.html",
        {
            "pet_business_detail": post,
            "comment_form": comment_form,
        },
    )