from django.urls import path
from .views import UserRegisterView, login

app_name = "accounts"

urlpatterns = [
    path('login/', login),
    path('registration/', UserRegisterView.as_view())
]

