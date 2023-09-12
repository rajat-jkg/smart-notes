from django.urls import path
from . import views
urlpatterns = [
    path('login', views.LoginInterface.as_view(), name='login'),
    path('logout', views.LogoutClass.as_view(), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),

]
