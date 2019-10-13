from django.urls import path
from .views import *

urlpatterns = [
    path('',blog_post_list_view),
    path('student/', get_student),
    path('show/',show),
    path('delete_student/<int:sid>/',delete_student),
    path('edit_student/<int:sid>/',edit_student),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/update/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
]
