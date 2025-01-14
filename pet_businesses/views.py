from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import PetBusiness, Comment, Like
from .forms import CommentForm, UserRegistrationForm, CustomSignupForm, PetBusinessForm
from .utils import group_required
from django.core.exceptions import PermissionDenied


# Custom signup view with group assignement

def custom_signup(request):
    """
    Custom signup view combining user registration and group assignment.
    """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        group_form = CustomSignupForm(request.POST)

        if user_form.is_valid() and group_form.is_valid():
            # Save the user
            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data['email']  # Save the email field
            user.save()

            # Assign the user to the selected group
            group_name = group_form.cleaned_data['group']
            try:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
                messages.success(request, "Account created successfully!")
                return redirect('login')  # Redirect to login page
            except Group.DoesNotExist:
                messages.error(request, f"The group '{group_name}' does not exist.")
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        user_form = UserRegistrationForm()
        group_form = CustomSignupForm()

    return render(request, 'registration/signup.html', {
        'user_form': user_form,
        'group_form': group_form,
    })


# Business list view

class BusinessList(generic.ListView):
    """
    View to render businesses list.
    """
    queryset = PetBusiness.objects.all()
    template_name = "pet_businesses/pet_business_list.html"
    context_object_name = "pet_business_list"
    paginate_by = 3


# Business detail and comment creation view

def pet_business_detail(request, slug):
    """
    View to render business details and create comments.
    """
    post = get_object_or_404(PetBusiness.objects.filter(approved=True),
                             slug=slug)
    comments = post.comments.all().order_by("-date_created")
    comment_count = post.comments.filter(approved=True).count()

    likes_count = post.likes.count()
    has_liked = post.likes.filter(author=request.user).exists() if request.user.is_authenticated else False

    if request.method == "POST":  # To create a comment
        if not request.user.groups.filter(name="Pet Owners").exists():
            raise PermissionDenied("You do not have permission to post comments.")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user  # To ensure the user is logged in
            comment.pet_businesse = post
            comment.save()
            messages.success(
                request, "Comment submitted and awaiting approval."
            )
            return HttpResponseRedirect(reverse('pet_business_detail', args=[slug]))
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

@group_required("Pet Owners")
def comment_edit(request, slug, comment_id):
    """
    View to edit comments.
    """
    if request.method == "POST":

        queryset = PetBusiness.objects.filter(approved=True)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.pet_business = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request,
                                 messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('pet_business_detail', args=[slug]))


# Comment deleting view

@group_required("Pet Owners")
def comment_delete(request, slug, comment_id):
    """
    View to delete comment.
    """
    queryset = PetBusiness.objects.filter(approved=True)
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


# Like adding or retriewing like

@group_required("Pet Owners")
def like_post(request, pet_business_id):
    pet_business = get_object_or_404(PetBusiness, id=pet_business_id)
    like, created = Like.objects.get_or_create(pet_business=pet_business,
                                               author=request.user)

    if not created:  # If the Like already exists, delete it (toggle)
        like.delete()

    return redirect('pet_business_detail', slug=pet_business.slug)


# Pet business creating view

@group_required("Business Owners")
def pet_business_form(request):
    """
    View to list pet businesses created by the logged-in user.
    """
    pet_businesses = PetBusiness.objects.filter(author=request.user)
    return render(request, 'pet_businesses/pet_business_form.html', {
        'pet_businesses': pet_businesses,
    })

