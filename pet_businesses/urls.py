from . import views
from django.urls import path

urlpatterns = [
    path('', views.BusinessList.as_view(), name='home'),
    path('<slug:slug>/', views.pet_business_detail, name='pet_business_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('pet-business/<int:pet_businesse_id>/like/', views.like_post, name='like_post'),
]