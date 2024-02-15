from django.urls import path
from board.views import board
from user.views import signin
from user.views import signup

urlpatterns = [
    path("", board, name="board"),
    path("user/signin", signin, name = "signin"),
    path("user/signup", signup, name="signup")
]