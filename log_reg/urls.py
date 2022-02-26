from django.urls import path     
from . import views
urlpatterns = [
    path('user_register', views.user_register),
    path('user_register/new', views.add_new_user),
    path('user_register/login', views.user_login),
    path('company_register', views.company_register),
    path('company_register/new', views.add_new_company),
    path('company_register/login', views.company_login),
]