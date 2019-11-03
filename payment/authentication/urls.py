from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
    path('registration/', views.Registration.as_view(), name='Registration'),
    path('saveuser/', views.SaveUser.as_view(), name='SaveUser')
]
