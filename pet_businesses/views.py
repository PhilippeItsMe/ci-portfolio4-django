from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Pet_Businesse,Comment
from .forms import Comment_Form


# Business list view

class Business_List(generic.ListView):
    """
    view to render businesses list
    """
    queryset = Pet_Businesse.objects.all()
    template_name = "pet_businesses/pet_business_list.html"
    context_object_name = "pet_business_list"
    paginate_by = 3


# Business detail view

def pet_business_detail(request, slug):
    """
    view to render business details
    """
    post = get_object_or_404(Pet_Businesse.objects.filter(approved=True), slug=slug)
    comments = post.comments.all().order_by("-date_created")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST": # To create a comment
        comment_form = Comment_Form(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user  # To ensure the user is logged in
            comment.pet_businesse = post
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting approval."
            )
            return render(
                request,
                "pet_businesses/pet_business_detail.html",
                {"pet_business_detail": post, "comment_count": comment_count,"comment_form": Comment_Form()},
            )
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        comment_form = Comment_Form()
     
    return render(
        request,
        "pet_businesses/pet_business_detail.html",
        {
            "pet_business_detail": post,
            "comment_form": comment_form,
            "comments": comments,
            "comment_count": comment_count,
        },
    )


# Comment editing view

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Pet_Businesse.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = Comment_Form(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('pet_business_detail', args=[slug]))


# Comment deleting view

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Pet_Businesse.objects.filter(approved=True)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('pet_business_detail', args=[slug]))