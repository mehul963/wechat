from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="Home"),
    path('login',views._login,name="login"),
    path('signup',views.signup,name="sign"),
    path('get_chat',views.get_chat,name="get_chat"),
    path('logout',views._logout,name="logout"),
]