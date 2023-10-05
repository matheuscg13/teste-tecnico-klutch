from .views import ListCreateUser, RetrieveUpdateDestroyUser
from django.urls import path


urlpatterns = [

    path("users/", ListCreateUser.as_view()),
    path(
        "users/<str:cpf>/",
        RetrieveUpdateDestroyUser.as_view(),
    ),
]
