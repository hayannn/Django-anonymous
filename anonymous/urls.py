from django.urls import path
from board.views import board, post_write
from user.views import signin, signup, sign_out

urlpatterns = [
    path("", board, name="board"),
    path("user/signin", signin, name = "signin"),
    path("user/signup", signup, name="signup"),
    path("user/signout", sign_out, name="signout"),
    path("post/write", post_write, name="post_write")
]