from .views import SolicitationView
from django.urls import path
from . import views



urlpatterns = [

    path("solicitations/", SolicitationView.as_view()),
    path('consult_installments/', views.ConsultInstallmentsView.as_view(), name='consult_installments'),

]
