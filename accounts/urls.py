from django.urls import path

from . import views

app_name = "autorization"
urlpatterns = [
    path("singup/", views.SignUpView.as_view(), name="signup"),
]