from django.urls import path

from Users.views import UserListCreate, UserDetailEditDelete
from Posts.views import PostListCreate, PostDetailEditDelete
from Posts.views import LikeCreate, LikeDelete


urlpatterns = [
    path("users/", UserListCreate.as_view(), name="Create and List"),
    path("users/<int:pk>/", UserDetailEditDelete.as_view(), name="Detail, Update and Delete"),
    path("careers/", PostListCreate.as_view(), name="Create and List"),
    path("careers/<int:pk>/", PostDetailEditDelete.as_view(), name="Detail, Update and Delete"),
    path("careers/likes/", LikeCreate.as_view()),
    path("careers/likes/<int:post_id>/<int:user_id>/", LikeDelete.as_view())
]
