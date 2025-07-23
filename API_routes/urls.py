from django.urls import path
from Users.views import UserListCreate, UserDetailEditDelete
from Posts.views import PostListCreate, PostDetailEditDelete


urlpatterns = [
    path("users/", UserListCreate.as_view(), name="Create and List"),
    path("users/<int:pk>/", UserDetailEditDelete.as_view(), name="Detail, Update and Delete"),
    path("careers/", PostListCreate.as_view(), name="Create and List"),
    path("careers/<int:pk>/", PostDetailEditDelete.as_view(), name="Detail, Update and Delete")
]