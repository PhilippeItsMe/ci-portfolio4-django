from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import PetBusinesse, Comment, Like
from .forms import CommentForm


# Business list view

class BusinessList(generic.ListView):
    """
    View to render businesses list.
    """
    queryset = PetBusinesse.objects.all()
    template_name = "pet_businesses/pet_business_list.html"
    context_object_name = "pet_business_list"
    paginate_by = 3


# Business detail view

def pet_business_detail(request, slug):
    """
    View to render business details.
    """
    post = get_object_or_404(PetBusinesse.objects.filter(approved=True),
                             slug=slug)
    comments = post.comments.all().order_by("-date_created")
    comment_count = post.comments.filter(approved=True).count()

    likes_count = post.likes.count()
    has_liked = post.likes.filter(author=request.user).exists() if request.user.is_authenticated else False

    if request.method == "POST":  # To create a comment
        comment_form = CommentForm(data=request.POST)
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
                {"pet_business_detail": post, "comment_count": comment_count,
                    "comment_form": CommentForm()},
            )
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        comment_form = CommentForm()

    return render(
        request,
        "pet_businesses/pet_business_detail.html",
        {
            "pet_business_detail": post,
            "comment_form": comment_form,
            "comments": comments,
            "comment_count": comment_count,
            "likes_count": likes_count,
            "has_liked": has_liked,
        },
    )


# Comment editing view

def comment_edit(request, slug, comment_id):
    """
    View to edit comments.
    """
    if request.method == "POST":

        queryset = PetBusinesse.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('pet_business_detail', args=[slug]))


# Comment deleting view

def comment_delete(request, slug, comment_id):
    """
    View to delete comment.
    """
    queryset = PetBusinesse.objects.filter(approved=True)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('pet_business_detail', args=[slug]))


# Like adding or retriewing view

@login_required
def like_post(request, pet_businesse_id):
    pet_business = get_object_or_404(PetBusinesse, id=pet_businesse_id)
    like, created = Like.objects.get_or_create(pet_businesse=pet_business,
                                               author=request.user)

    if not created:  # If the Like already exists, delete it (toggle)
        like.delete()

    return redirect('pet_business_detail', slug=pet_business.slug)
