from django.urls import path
from .views import ListOfPosts, SinglePost

urlpatterns = [
    path('', ListOfPosts.as_view(), name='listofposts'),
    path('post/<int:pk>/', SinglePost.as_view(), name='singlepost'),
]
