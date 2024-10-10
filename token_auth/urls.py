from django.urls import path
from . import views

urlpatterns = [
    path("api-token-auth/", views.HelloView.as_view()),
    path("api/auth/register/", views.RegistrationView.as_view()),
]
