from django.urls import path
from .views import *

urlpatterns = [
    path('login/',userLogin,name="login"),
    path('browse/',profiles,name="browse"),
    path('register/',register,name="register"),
    path('create-profile/',createProfile,name="createProfile"),
    path('logout/',userLogout,name="logout"),
    path('hesap/',userAccount,name="hesap"),
    path('user-delete',userDelete,name="delete")
]
